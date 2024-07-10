import tkinter as tk
import random
import time
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SmartLight:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = False  # Light is initially off
        self.brightness = 0  # Brightness level (0-100)

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def set_brightness(self, brightness):
        self.brightness = max(0, min(100, brightness))  # Ensure brightness is within 0-100 range

    def randomize(self):
        if self.status:
            # Simulate gradual dimming or brightening
            self.brightness += random.randint(-5, 5)
            self.brightness = max(0, min(100, self.brightness))

class Thermostat:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = False  # Thermostat is initially off
        self.temperature = 72  # Default temperature (in °F)
        self.min_temperature = 60  # Minimum temperature
        self.max_temperature = 80  # Maximum temperature

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def set_temperature(self, temperature):
        self.temperature = max(self.min_temperature, min(self.max_temperature, temperature))

    def randomize(self):
        if self.status:
            # Simulate gradual temperature changes
            self.temperature += random.randint(-1, 1)

class SecurityCamera:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = False  # Camera is initially off
        self.security_status = "Disarmed"

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def arm(self):
        self.security_status = "Armed"

    def disarm(self):
        self.security_status = "Disarmed"

    def randomize(self):
        if self.status:
            # Simulate changes in security status
            if random.random() < 0.1:
                self.security_status = "Alert"

class AutomationSystem:
    def __init__(self):
        self.devices = []  # List to store registered devices
        self.gui = None  # Reference to the GUI instance

    def discover_device(self, device):
        # Add a new device to the system
        self.devices.append(device)

    def execute_automation_task(self):
        for device in self.devices:
            # Define your automation rules and tasks here
            if isinstance(device, SmartLight):
                if random.random() < 0.1:
                    device.turn_on()
                else:
                    device.turn_off()
            elif isinstance(device, Thermostat):
                device.set_temperature(random.uniform(60, 80))
            elif isinstance(device, SecurityCamera):
                if random.random() < 0.1:
                    device.arm()
                else:
                    device.disarm()

    def simulation_loop(self, interval_seconds, gui):
        self.gui = gui  # Set the reference to the GUI instance
        while True:
            self.execute_automation_task()

            for device in self.devices:
                device.randomize()

            # You can update your GUI here to reflect the latest device states

            time.sleep(interval_seconds)

    def pause_simulation(self):
        self.gui = None  # Remove the reference to the GUI instance

class SmartHomeGUI:
    def __init__(self, root, automation_system):
        self.root = root
        self.root.title("Smart Home Monitoring Dashboard")

        self.automation_system = automation_system

        self.device_frames = []  # To store frames for individual devices

        # Create the main dashboard frame
        self.dashboard_frame = tk.Frame(root)
        self.dashboard_frame.pack()

        # Create a button to start/pause the simulation
        self.start_button = tk.Button(self.dashboard_frame, text="Start Simulation", command=self.toggle_simulation)
        self.start_button.pack()

        # Create a frame for each device
        for device in automation_system.devices:
            device_frame = tk.Frame(self.dashboard_frame)
            device_frame.pack()
            self.device_frames.append(device_frame)

        # Start the GUI update loop
        self.update_gui()

    def toggle_simulation(self):
        # Start or pause the simulation loop
        if self.start_button.cget("text") == "Start Simulation":
            self.start_button.config(text="Pause Simulation")
            self.automation_system.simulation_loop(interval_seconds=5, gui=self)
        else:
            self.start_button.config(text="Start Simulation")
            self.automation_system.pause_simulation()

    def update_gui(self):
        # Update the GUI with the latest device states and properties
        for idx, device in enumerate(self.automation_system.devices):
            device_frame = self.device_frames[idx]

            # Update the device status and properties
            status_label = tk.Label(device_frame, text=f"Status: {'On' if device.status else 'Off'}")
            status_label.pack()

            if isinstance(device, SmartLight):
                brightness_label = tk.Label(device_frame, text=f"Brightness: {device.brightness}")
                brightness_label.pack()

            if isinstance(device, Thermostat):
                temperature_label = tk.Label(device_frame, text=f"Temperature: {device.temperature}°F")
                temperature_label.pack()

            if isinstance(device, SecurityCamera):
                security_label = tk.Label(device_frame, text=f"Security Status: {device.security_status}")
                security_label.pack()

        # Schedule the GUI update every 1 second
        self.root.after(1000, self.update_gui)

if __name__ == "__main__":
    automation_system = AutomationSystem()

    # Add devices to the automation system
    light = SmartLight(1)
    thermostat = Thermostat(2)
    camera = SecurityCamera(3)

    automation_system.discover_device(light)
    automation_system.discover_device(thermostat)
    automation_system.discover_device(camera)

    root = tk.Tk()
    gui = SmartHomeGUI(root, automation_system)

    root.mainloop()

import tkinter as tk
from tkinter import ttk
import random

class IoTDevice:
    def __init__(self, device_id, status=False):
        self.device_id = device_id
        self.status = status

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def __str__(self):
        return f"Device ID: {self.device_id}, Status: {'On' if self.status else 'Off'}"
   

class SmartLight(IoTDevice):
    def __init__(self, device_id, brightness=0):
        super().__init__(device_id)
        self.brightness = brightness

    def change_brightness(self, new_brightness):
        self.brightness = new_brightness

    def randomize_behavior(self):
        if self.status:
            self.brightness = random.randint(0, 100)

    def __str__(self):
        return super().__str__() + f", Brightness: {self.brightness}"

class Thermostat(IoTDevice):
    def __init__(self, device_id, temperature=20.0):
        super().__init__(device_id)
        self.temperature = temperature

    def set_temperature(self, new_temperature):
        self.temperature = new_temperature

    def randomize_behavior(self):
        self.temperature += random.uniform(-1, 1)

    def __str__(self):
        return super().__str__() + f", Temperature: {self.temperature}°C"

class SecurityCamera(IoTDevice):
    def __init__(self, device_id, security_status="Idle"):
        super().__init__(device_id)
        self.security_status = security_status

    def set_security_status(self, new_status):
        self.security_status = new_status

    def randomize_behavior(self):
        statuses = ["Idle", "Recording", "Alert"]
        self.security_status = random.choice(statuses)

    def __str__(self):
        return super().__str__() + f", Security Status: {self.security_status}"

class SmartHomeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Home Control Panel")

        self.devices = [
            SmartLight("Light"),
            Thermostat("Thermostat"),
            SecurityCamera("SecurityCamera")
        ]

        self.create_gui()
        self.update_status()
        
    def save_data_to_file(self, filename="smart_home_data.txt"):
        with open(filename, 'w') as file:
            for device in self.devices:
                file.write(str(device) + "\n")


    def create_gui(self):
        for device in self.devices:
            frame = ttk.LabelFrame(self.root, text=device.device_id)
            frame.grid(padx=10, pady=5, sticky="w")

            status_label = ttk.Label(frame, text="Status:")
            status_label.grid(row=0, column=0, sticky="w")

            status_var = tk.StringVar()
            status_var.set("On" if device.status else "Off")
            status = ttk.Label(frame, textvariable=status_var)
            status.grid(row=0, column=1, sticky="w")

            toggle_button = ttk.Button(frame, text="Toggle", command=lambda d=device: self.toggle_device(d))
            toggle_button.grid(row=1, column=0, columnspan=2, pady=5)

            if isinstance(device, SmartLight):
                brightness_label = ttk.Label(frame, text="Brightness:")
                brightness_label.grid(row=2, column=0, sticky="w")

                brightness_var = tk.StringVar()
                brightness_var.set(device.brightness)
                brightness = ttk.Label(frame, textvariable=brightness_var)
                brightness.grid(row=2, column=1, sticky="w")

                brightness_slider = ttk.Scale(frame, from_=0, to=100, orient="horizontal", variable=brightness_var)
                brightness_slider.grid(row=3, column=0, columnspan=2, pady=5)

            elif isinstance(device, Thermostat):
                temperature_label = ttk.Label(frame, text="Temperature:")
                temperature_label.grid(row=2, column=0, sticky="w")

                temperature_var = tk.DoubleVar()
                temperature_var.set(device.temperature)
                temperature = ttk.Label(frame, textvariable=temperature_var)
                temperature.grid(row=2, column=1, sticky="w")

                temperature_slider = ttk.Scale(frame, from_=10, to=30, orient="horizontal", variable=temperature_var)
                temperature_slider.grid(row=3, column=0, columnspan=2, pady=5)

            elif isinstance(device, SecurityCamera):
                status_label = ttk.Label(frame, text="Security Status:")
                status_label.grid(row=2, column=0, sticky="w")

                status_var = tk.StringVar()
                status_var.set(device.security_status)
                status = ttk.Label(frame, textvariable=status_var)
                status.grid(row=2, column=1, sticky="w")

                toggle_button = ttk.Button(frame, text="Toggle", command=lambda d=device: self.toggle_device(d))
                toggle_button.grid(row=3, column=0, columnspan=2, pady=5)

                analyze_button = ttk.Button(self.root, text="Analyze Data", command=self.analyze_data)
                analyze_button.grid(row=len(self.devices), columnspan=2, pady=10)

                # Add slider for Security Camera
                security_slider = ttk.Scale(frame, from_=0, to=100, orient="horizontal", variable=tk.DoubleVar())
                security_slider.grid(row=4, column=0, columnspan=2, pady=5)

    def toggle_device(self, device):
        device.status = not device.status
        self.update_status()

    def update_status(self):
        for device in self.devices:
            if isinstance(device, SmartLight):
                device.randomize_behavior()
                status_label = device.device_id
                for frame in self.root.winfo_children():
                    if frame['text'] == device.device_id:
                        for child in frame.winfo_children():
                            if "Brightness:" in child['text']:
                                child['text'] = "Brightness: " + str(device.brightness)
                            elif "Status:" in child['text']:
                                child['text'] = "Status: " + ("On" if device.status else "Off")
            
            elif isinstance(device, Thermostat):
                device.randomize_behavior()
                status_label = device.device_id
                for frame in self.root.winfo_children():
                    if frame['text'] == device.device_id:
                        for child in frame.winfo_children():
                            if "Temperature:" in child['text']:
                                child['text'] = "Temperature: " + str(device.temperature) + "°C"
                            elif "Status:" in child['text']:
                                child['text'] = "Status: " + ("On" if device.status else "Off")
            
            elif isinstance(device, SecurityCamera):
                device.randomize_behavior()
                status_label = device.device_id
            for frame in self.root.winfo_children():
                if frame['text'] == device.device_id:
                    for child in frame.winfo_children():
                        if "Security Status:" in child['text']:
                            child['text'] = "Security Status: " + device.security_status

    def analyze_data(self):
        on_devices = [device for device in self.devices if device.status]
        off_devices = [device for device in self.devices if not device.status]
        num_on_devices = len(on_devices)
        num_off_devices = len(off_devices)

        analysis_result = f"Number of On Devices: {num_on_devices}\n" \
                         f"Number of Off Devices: {num_off_devices}"

        analysis_label = ttk.Label(self.root, text=analysis_result)
        analysis_label.grid()

        if num_on_devices > num_off_devices:
            suggestion = "Suggestion: Turn off some devices to save energy."
        elif num_on_devices < num_off_devices:
            suggestion = "Suggestion: Turn on some devices for better security or comfort."
        else:
            suggestion = "No specific suggestions."

        suggestion_label = ttk.Label(self.root, text=suggestion)
        suggestion_label.grid()
        
        print(suggestion)
        
      
if __name__ == "__main__":
    root = tk.Tk()
    app = SmartHomeGUI(root)
    root.mainloop()

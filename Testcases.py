import unittest
import tkinter as tk
from unittest.mock import patch
from io import StringIO
from IOIT import SmartLight, Thermostat, SecurityCamera, SmartHomeGUI

class TestSmartHomeGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = SmartHomeGUI(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_toggle_device(self):
        # Test for SmartLight
        smart_light = self.app.devices[0] 
        initial_status = smart_light.status
        self.app.toggle_device(smart_light)
        self.assertNotEqual(smart_light.status, initial_status)

        # Test for Thermostat
        thermostat = self.app.devices[1]
        initial_status = thermostat.status
        self.app.toggle_device(thermostat)
        self.assertNotEqual(thermostat.status, initial_status)

        # Test for SecurityCamera
        security_camera = self.app.devices[2]
        initial_status = security_camera.status
        self.app.toggle_device(security_camera)
        self.assertNotEqual(security_camera.status, initial_status)

    def test_update_status(self):
        # Create a test SmartLight device
        smart_light = SmartLight("TestLight", brightness=50)
        self.app.devices.append(smart_light)
        self.app.update_status()
        for frame in self.root.winfo_children():
            if "TestLight" in frame['text']:
                for child in frame.winfo_children():
                    if "Brightness:" in child['text']:
                        self.assertIn("Brightness:", child["text"])
                    elif "Status:" in child['text']:
                        self.assertIn("Status:", child["text"])

    @patch('sys.stdout', new_callable=StringIO)
    def test_analyze_data(self, mock_stdout):
        # Test with all devices off
       # Test with all devices off
        self.app.devices[0].turn_off()
        self.app.devices[1].turn_off()
        self.app.devices[2].turn_off()
        self.app.analyze_data()
        expected_output = "Suggestion: Turn on some devices for better security or comfort.\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

        # Test with more devices on
        self.app.devices[1].turn_on()
        self.app.analyze_data()
        expected_output = "Suggestion: Turn off some devices to save energy.\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_create_gui(self):
        self.assertEqual(len(self.root.winfo_children()), len(self.app.devices) + 1)  

if __name__ == "__main__":
    unittest.main()

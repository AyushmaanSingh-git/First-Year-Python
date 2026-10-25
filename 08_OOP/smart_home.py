# Question 8: Smart Home Device Control
# Concepts: Classes, inheritance, function overriding, super()
# Scenario: A smart home system controls different devices. Every device can be
# switched on, but an air conditioner also displays its cooling temperature when
# switched on.
# Task: Create a SmartDevice class with a turn_on() method. Override it in the
# AirConditioner class and call the parent's method using super().
# Sample input:
# Device: Air Conditioner
# Temperature: 22
# Expected output:
# Device is switched on
# Air Conditioner cooling at 22 degrees

class SmartDevice:
    def turn_on(self):
        print("Device is switched on")

class AirConditioner(SmartDevice):
    def __init__(self, temperature):
        self.temperature = temperature

    def turn_on(self):
        super().turn_on()
        print(f"Air Conditioner cooling at {self.temperature} degrees")

device_type = input("Device: ")
if device_type.lower() == "air conditioner":
    temperature = int(input("Temperature: "))
    device = AirConditioner(temperature)
else:
    device = SmartDevice() 

device.turn_on()

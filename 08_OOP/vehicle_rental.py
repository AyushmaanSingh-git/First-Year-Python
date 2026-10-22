# Question 3: Vehicle Rental System
# Concepts: Classes, inheritance, method overriding
# Scenario: A rental company rents cars and bikes. The rental charge depends on
# the type of vehicle. A car costs ₹2,000 per day, while a bike costs ₹500 per day.
# Task: Create a parent class Vehicle and child classes Car and Bike. Override
# calculate_rent() in each child class.
# Sample input:
# Vehicle: Car
# Days: 3
# Expected output:
# Vehicle: Car
# Total Rent: 6000

class Vehicle:
    def __init__(self,days):
        self.days = days

    def calculate_rent(self):
        pass

class Car(Vehicle):
    def calculate_rent(self):
        return self.days * 2000

class Bike(Vehicle):
    def calculate_rent(self):
        return self.days * 500

vehicle_type = input("Vehicle Type(Car/Bike):")
days = int(input("Days: "))

if vehicle_type.lower() == "car":
    vehicle = Car(days)
elif vehicle_type.lower() =="bike":
    vehicle = Bike(days)
else:
    print("Invalid vehicle type")
    exit()

print("Vehicle:", vehicle_type.capitalize())
print("Total Rent:", vehicle.calculate_rent())
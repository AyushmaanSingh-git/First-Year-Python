# Question 6: Hospital Billing System
# Concepts: Inheritance, method overriding, super()
# Scenario: A hospital charges a standard consultation fee of ₹500. A specialist
# charges the standard fee plus an additional specialist fee of ₹800.
# Task: Create a Doctor class with calculate_fee(). Override it in SpecialistDoctor
# and use super() to calculate the total fee.
# Sample input:
# Consultation Fee: 500
# Specialist Fee: 800
# Expected output:
# Total Consultation Fee: 1300

class Doctor:
    def __init__(self, consultation_fee):
        self.consultation_fee = consultation_fee

    def calculate_fee(self):
        return self.consultation_fee

class SpecialistDoctor(Doctor):
    def __init__(self, consultation_fee, specialist_fee):
        super().__init__(consultation_fee)
        self.specialist_fee = specialist_fee

    def calculate_fee(self):
        base_fee = super().calculate_fee()
        return base_fee + self.specialist_fee

consultation_fee = float(input("Consultation Fee: "))
specialist_fee = float(input("Specialist Fee: "))

doctor_type = input("Doctor Type(General/Specialist): ")
if doctor_type.lower() == "general":
    doctor = Doctor(consultation_fee)
elif doctor_type.lower() == "specialist":
    doctor = SpecialistDoctor(consultation_fee, specialist_fee)
else:
    print("Invalid doctor type")
    exit()
# Question 9: Digital Payment System
# Concepts: Inheritance, function overriding, super()
# Scenario: A digital payment application supports UPI and credit card payments.
# Every transaction has a base processing fee of ₹5. Credit card payments incur an
# additional fee of 2% of the transaction amount.
# Task: Create a parent class Payment and a child class CreditCardPayment.
# Override calculate_fee() and use super() to obtain the base processing fee.
# Sample input:
# Payment Amount: 1000
# Expected output:
# Processing Fee: 25.0
# Total Payable: 1025.0

class Payment:
    def __init__(self, amount):
        self.amount = amount

    def calculate_fee(self):
        return 5  # Base processing fee

class CreditCardPayment(Payment):
    def calculate_fee(self):
        base_fee = super().calculate_fee()
        additional_fee = 0.02 * self.amount  # 2% of the transaction amount
        return base_fee + additional_fee

payment_amount = float(input("Payment Amount: "))
payment_type = input("Payment Type(UPI/Credit Card): ")
if payment_type.lower() == "upi":
    payment = Payment(payment_amount)
elif payment_type.lower() == "credit card":
    payment = CreditCardPayment(payment_amount)
else:
    print("Invalid payment type")
    exit()
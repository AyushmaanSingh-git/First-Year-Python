# Question 2: Online Shopping Discount System
# Concepts: Inheritance, function overriding, super()
# Scenario: An online shopping platform offers different discounts. A normal
# customer receives a 5% discount, while a premium customer receives a 15%
# discount.
# Task: Create a Customer class with a final_price() method. Override this
# method in the PremiumCustomer class and use super() to reuse the parent's
# calculation.
# Sample input:
# Product Price: 2000
# Customer Type: Premium
# Expected output:
# Original Price: 2000
# Final Price: 1700.0

class Customer:
    def __init__(self,price):
        self.price = price

    def final_price(self):
        return self.price-(self.price*5/100)

class PremiumCustomer(Customer):
    def final_price(self):
        return super().final_price() - (self.price * 10/100)

customer = PremiumCustomer(2000)

print("Original Price:", customer.price)
print("Final Price:",customer.final_price())
    
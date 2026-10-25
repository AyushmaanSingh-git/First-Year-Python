# Question 7: Food Delivery Charges
# Concepts: Classes, inheritance, method overriding
# Scenario: A food delivery application charges a standard delivery fee of ₹40.
# Express delivery costs ₹40 plus an additional ₹60.
# Task: Create a parent class Delivery and a child class ExpressDelivery. Override
# calculate_charge() in the child class.
# Sample input:
# Delivery Type: Express
# Order Amount: 500
# Expected output:
# Delivery Charge: 100
# Total Amount: 600

class Delivery:
    def __init__(self, delivery_fee):
        self.delivery_fee = delivery_fee

    def calculate_charge(self):
        return self.delivery_fee

class ExpressDelivery(Delivery):
    def __init__(self, delivery_fee, express_fee):
        super().__init__(delivery_fee)
        self.express_fee = express_fee

    def calculate_charge(self):
        base_charge = super().calculate_charge()
        return base_charge + self.express_fee

delivery_type = input("Delivery Type(Standard/Express): ")
order_amount = float(input("Order Amount: "))
if delivery_type.lower() == "standard":
    delivery = Delivery(40)
elif delivery_type.lower() == "express":
    delivery = ExpressDelivery(40, 60)
else:
    print("Invalid delivery type")
    exit()
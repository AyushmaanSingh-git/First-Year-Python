name = input("Name? ")
roll_no = int(input("Roll no? "))

if name == "Rahul" and roll_no == 17:
    print("You are allowed to sit in Section B")
elif name == "Subham" and roll_no == 30:
    print("You are allowed to sit in Section D")
else:
    print("No seating assignment found.")
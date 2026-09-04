phy = int(input("Enter your Physics Marks: "))
chem = int(input("Enter your Chemistry Marks: "))
math = int(input("Enter your Mathematics Marks: "))
eng = int(input("Enter your English Marks: "))
opt = int(input("Enter your Optional Subject Marks: "))

Total = (phy + chem + math + eng + opt) / 500 * 100
print("Your percentage is", Total)

fee = int(input("Please Enter Your Total Fees: "))

if Total >= 95 and Total <= 100:
    rebate1 = (20 / 100) * fee
    fees1 = fee - rebate1
    print("Your fees is Rs", fees1)
elif Total >= 85 and Total < 95:
    rebate2 = (15 / 100) * fee
    fees2 = fee - rebate2
    print("Your fees is Rs", fees2)
elif Total >= 75 and Total < 85:
    rebate3 = (10 / 100) * fee
    fees3 = fee - rebate3
    print("Your fees is Rs", fees3)
elif Total < 75:
    print("No Rebate, Your fees is Rs", fee)
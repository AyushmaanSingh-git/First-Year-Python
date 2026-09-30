# Develop a python program to check if no. is a perfect no. or not.
num = int(input("Enter a no. "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum = sum + i
        
if sum == num:
    print("No. is perfect ")
else:
    print("No. is not perfect ")
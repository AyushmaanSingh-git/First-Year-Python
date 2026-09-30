# WAPP to print factorial of a number n
n = int(input("Enter a number: "))
r = 1

for i in range(1, n+1):
    r = r * i
    
print("The factorial is ", r)
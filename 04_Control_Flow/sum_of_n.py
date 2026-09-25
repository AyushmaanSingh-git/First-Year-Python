# Write a python program to print sum of 1 to n
n = int(input("Enter a natural no. "))
s = 0

for i in range(1, n+1, 1):
    s = s + i
    
print(s)
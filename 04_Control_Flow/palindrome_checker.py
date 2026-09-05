n = int(input("enter a no. "))

tmp = n
rev = 0

while n != 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10
    
if rev == tmp:
    print("pm")
else:
    print("npm")
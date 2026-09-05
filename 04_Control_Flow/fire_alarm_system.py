t = int(input("What is the temperature in C?"))
s = input("is there smoke ? yes or no ??")
b = input("on or off ??")

if (s == "yes" and t >= 65 or b == "on"):
    print("Alarm Ringing")
else:
    print("you are safe")
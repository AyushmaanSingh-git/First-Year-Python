# --- WHOLE NUMBERS ---
print("--- Whole Numbers ---")
num = int(input("Enter your no. : "))
i = 0
print("These are whole no's:")
while i <= num:
    print(i)
    i = i + 1

# --- EVEN NUMBERS ---
print("\n--- Even Numbers ---")
num = int(input("Enter your limit: "))

# Method 1
i = 0
print("These are even no's (Method 1):")
while i <= num:
    print(i)
    i = i + 2

# Method 2
i = 0
print("These are even no's (Method 2):")
while i <= num:
    if i % 2 == 0:
        print(i)
    i = i + 1

# --- ODD NUMBERS ---
print("\n--- Odd Numbers ---")
num = int(input("Enter your limit: "))

# Method 1
i = 1
print("These are odd no's (Method 1):")
while i <= num:
    print(i)
    i = i + 2

# Method 2
i = 0
print("These are odd no's (Method 2):")
while i <= num:
    if i % 2 != 0:
        print(i)
    i = i + 1
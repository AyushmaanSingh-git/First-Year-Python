# QUESTION 3: Write a menu-driven program for the choices entered by the user:
# i) Factorial of a no (comparing Loop vs Recursion)
# ii) Sum of whole numbers up to n (using Recursion)
# STUDY NOTE: This script skips temporary variables like 'a = factorialF(value)' 
# and prints the return values directly to keep the code clean.

# --- FUNCTION DEFINITIONS ---

def factorialF(value):
    # Calculates factorial using a standard for-loop (Iterative method)
    fact = 1
    for i in range(1, value + 1):
        fact = fact * i
    return fact

def factorialR(value):
    # Calculates factorial using recursion (calling itself)
    if value == 0 or value == 1:
        return 1
    return value * factorialR(value - 1)

def sumofseries(value):
    # Calculates the sum of 1 to 'value' using recursion
    if value == 1:
        return 1
    return value + sumofseries(value - 1)


# --- MAIN PROGRAM MENU ---

print("--- MENU ---")
print("1. Factorial using For Loop (factorialF)")
print("2. Factorial using Recursion (factorialR)")
print("3. Sum of series (1+2+3...+n) using Recursion (sumofseries)")

# Get the user's choice and the target number
choice = int(input("Enter your choice (1, 2, or 3): "))
value = int(input("Enter your value: "))

# Execute based on user's choice, printing the returned value immediately
if choice == 1:
    print("Result (Loop):", factorialF(value))
    
elif choice == 2:
    print("Result (Recursion):", factorialR(value))
    
elif choice == 3:
    print("Result (Sum):", sumofseries(value))
    
else:
    print("Invalid choice")
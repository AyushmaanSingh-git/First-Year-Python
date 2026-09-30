# QUESTION 1: Implement factorial using recursion.
# STUDY NOTE: A factorial (n!) is n * (n-1) * (n-2) ... * 1. 
# Recursion solves this by having the function call itself with a smaller number.

def fact(n):
    # 1. THE BASE CASE (Stopping Condition)
    # If we reach 1 or 0, we stop calling the function and just return 1.
    # Without this safety net, the program would call itself forever and crash!
    if n == 1 or n == 0:
        return 1
        
    # 2. THE RECURSIVE STEP
    # The function pauses, and calls itself with (n-1). 
    # Example for n=3: It returns 3 * fact(2)
    return n * fact(n - 1)

# Gather input from the user outside the function
num = int(input("Enter a number to find its factorial: "))

# Call the function and print the returned answer directly
print("The factorial is:", fact(num))
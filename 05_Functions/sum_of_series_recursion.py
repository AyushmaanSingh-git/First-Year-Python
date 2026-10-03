# QUESTION 2: Implement sum of whole numbers up to n (1+2+3...+n) using recursion.
# STUDY NOTE: Instead of a loop adding numbers to a bucket, we return 'n' plus the sum of '(n-1)'.

def sum_of_series(n):
    # 1. THE BASE CASE
    # The smallest whole number we are adding is 1, so if n reaches 1, return 1 and stop.
    if n == 1:
        return 1
        
    # 2. THE RECURSIVE STEP
    # Add the current number (n) to the result of the function called with (n-1).
    # Example for n=3: It returns 3 + sum_of_series(2)
    return n + sum_of_series(n - 1)

# Gather input from the user
num = int(input("Enter a limit for the sum: "))
print("The sum of the series is:", sum_of_series(num))
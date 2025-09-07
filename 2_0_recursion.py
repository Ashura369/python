# Recursive function to calculate factorial

def factorial(n):
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive case
    return n * factorial(n - 1)

# Test
print(factorial(5))   # Output: 120

# Recursion in Python
# A function calling itself to solve a problem.

# Example: Factorial using Recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
 
print(factorial(5)) 
# Must have a base case to avoid infinite recursion.
# Used in algorithms like Fibonacci, Tree Traversals.
# What are For Loops?
# For loops are used to iterate over a sequence (e.g., list, string, range).
# They execute a block of code repeatedly for each item in the sequence.
# for item in sequence:
    # Code to execute for each item
# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(fruit)
# Using range():
# The range() function generates a sequence of numbers.
# Example:
# for i in range(5,0,-1):
#     print(i)  # Output: 0, 1, 2, 3, 4    
# What are While Loops?
# While loops execute a block of code as long as a condition is True.
# They are useful when the number of iterations is not known in advance.
# Syntax:
# while condition:
#     # Code to execute while condition is True
# count = 1

# while count <= 5:
#     print(count)
#     count += 1
# Infinite Loops:
# Be careful to avoid infinite loops by ensuring the condition eventually becomes False.
# Example of an infinite loop:
while True:
    print("This will run forever!")
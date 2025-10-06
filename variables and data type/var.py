# Variables are used to store data that can be used and manipulated in a program.
# A variable is created when you assign a value to it using the = operator.
# Example:
# name = "Alice"
# age = 25
# height = 5.6
# like container to store things
#dynamically typed language
# rules of defining a variables in python
# Variable names can contain letters, numbers, and underscores.
# Variable names must start with a letter or underscore.
# Variable names are case-sensitive.
# Avoid using Python keywords as variable names (e.g., print, if, else).
# age=32 -> valid
# 23age=78 -> invalid
# ag$$e=98 -> invalid
# a_B_C=9 -> valid

# Data types Built in 
# Integers (int): Whole numbers (e.g., 10, -5).
# Floats (float): Decimal numbers (e.g., 3.14, -0.001).
# Strings (str): Text data enclosed in quotes (e.g., "Hello", 'Python').
# Booleans (bool): Represents True or False.
# Lists: Ordered, mutable collections (e.g., [1, 2, 3]).
# Tuples: Ordered, immutable collections (e.g., (1, 2, 3)).
# Sets: Unordered collections of unique elements (e.g., {1, 2, 3}).
# Dictionaries: Key-value pairs (e.g., {"name": "Alice", "age": 25})
# Checking Data Types
# Use the type() function to check the data type of a variable
print(type(10))       # Output: <class 'int'>
print(type("Hello"))  # Output: <class 'str'>
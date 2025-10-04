# Exceptions are events that occur during the execution of a program that disrupt the normal flow of instructions. Python provides a robust mechanism for handling exceptions using try-except blocks. This allows your program to gracefully recover from errors or unexpected situations, preventing crashes and providing informative error messages. You can also define your own custom exceptions to represent specific error conditions in your application.

# Basic Exception Handling
# The try-except block is the fundamental construct for handling exceptions:

# The try block contains the code that might raise an exception.

# The except block contains the code that will be executed if a specific exception occurs within the try block
# while True:
#     try:
#         a=int(input("enter the first number  "))
#         b=int(input("enter the second number  "))
#         print(f"the sum is {a+b}")
#     except Exception as e:
#           print("Some Error Occurred!! ", e)  

# Raising Exceptions (raise)
# You can manually raise exceptions using the raise keyword. This is useful for signaling error conditions in your own code.
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older!")
    return "Access granted."

try:
  print(check_age(20))  # Access granted.
  print(check_age(16))  # Raises ValueError
except ValueError as e:
  print(f"Error: {e}")

# try-except blocks are essential for handling errors and preventing program crashes.
# Multiple except blocks or a tuple of exception types can be used to handle different kinds of errors.
# The else block executes only if no exception occurs in the try block.
# The finally block always executes, making it suitable for cleanup tasks.
# The raise keyword allows you to manually trigger exceptions.
# Custom exceptions (subclasses of Exception) provide a way to represent application-specific errors and improve error handling clarity.

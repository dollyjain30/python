# *args and **kwargs are special syntaxes in Python function definitions that allow you to pass a variable number of arguments to a function. They are used when you don't know in advance how many arguments a function might need to accept.

# *args: Allows you to pass a variable number of positional arguments.
# **kwargs: Allows you to pass a variable number of keyword arguments.
#args will be a tuple of all the values passed to sum
# def sum(*args):
#     print(args)
#     total=0
#     for i in args:
#         total+=i
#     print(total)

# sum(23,78,654)    
def marks(**kwargs):
    for item in kwargs.keys():
        print(kwargs[item])
marks(rahul=90,vikrant=93,ram=92)  
# Flexible Function Design: *args and **kwargs make your functions more flexible, allowing them to handle a varying number of inputs without needing to define a specific number of parameters.
# Decorator Implementation: Decorators often use *args and **kwargs to wrap functions that might have different signatures.
# Function Composition: You can use *args and **kwargs to pass arguments through multiple layers of function calls.
# Inheritance: Subclasses can accept extra parameters to those defined by parent classes.      
# Example showing use in inheritance
class Animal:
  def __init__(self, name):
    self.name = name

class Dog(Animal):
  def __init__(self, name, breed, *args, **kwargs):
    super().__init__(name)
    self.breed = breed
    # Process any additional arguments or keyword arguments here
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Labrador", 1,2,3, color="Black", age = 5)
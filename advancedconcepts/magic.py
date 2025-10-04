# Magic methods, also called dunder (double underscore) methods, are special methods in Python that have double underscores at the beginning and end of their names (e.g., __init__, __str__, __add__). These methods allow you to define how your objects interact with built-in Python operators, functions, and language constructs. They provide a way to implement operator overloading and customize the behavior of your classes in a Pythonic way.
# Customize object creation and initialization (__init__, __new__).
# Enable operator overloading (e.g., +, -, *, ==, <, >).
# Provide string representations of objects (__str__, __repr__).
# Control attribute access (__getattr__, __setattr__, __delattr__).
# Make objects callable (__call__).
# Implement container-like behavior (__len__, __getitem__, __setitem__, __delitem__, __contains__).
# Support with context managers (__enter__,__exit__)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def __str__(self):
        return f"Person({self.name}, {self.age})"  # User-friendly
 
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"  # Unambiguous, for debugging
 
p = Person("Alice", 30)
print(str(p))    # Person(Alice, 30)
print(repr(p))   # Person(name='Alice', age=30)
print(p)          # Person(Alice, 30)  # print() uses __str__ if available
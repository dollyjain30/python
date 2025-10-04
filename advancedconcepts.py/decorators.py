# Decorators in Python are a powerful and expressive feature that allows you to modify or enhance functions and methods in a clean and readable way.
# Decorators use Python's higher-order function capability, meaning functions can accept other functions as arguments and return new functions.
# decorator is function that takes a function , it creates a new function inside its bidy (wrapper) . then it returns that new function

# def decorator(func):
#     def wrapper():
#         print("iam about to execute a function ...")
#         func()
#         print("i have executed this function")
#     return wrapper  
# @decorator
# def say_hello():
#     print("heello")
# say_hello()    
# f=decorator(say_hello)#this is also a function 
# f()
#after executing the code the f fuction looks like :
# def f():
# print("iam about to execute a function ...")
#  print("heello")
# print("i have executed this function")  
# # def say_hello():
#     print("heello")
# say_hello()    





#decorators with arguments
def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("world")




# Decorators are a key feature in Python that enable code reusability and cleaner function modifications. They are commonly used for:

# Logging: Recording when a function is called and its arguments.
# Timing: Measuring how long a function takes to execute.
# Authentication and Authorization: Checking if a user has permission to access a function.
# Caching: Storing the results of a function call so that subsequent calls with the same arguments can be returned quickly.
# Rate Limiting: Controlling how often a function can be called.
# Input Validation: Checking if the arguments to a function meet certain criteria.
# Instrumentation: Adding monitoring and profiling to functions.
# Frameworks like Flask and Django use decorators extensively for routing, authentication, and defining middleware.
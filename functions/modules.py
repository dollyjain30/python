# Modules and pip - Using External Libraries
# built in like math and external modules

# Importing Modules
# Python provides built-in and third-party modules.

# Example: Using the math module
# import math
# print(math.sqrt(16))  # Output: 4.0
# Creating Your Own Module

#Save this as mymodule.py:

# import mymodule
# print(mymodule.greet("Dolly"))
# Installing External Libraries with pip
# pip install requests

# Example usage:

import requests
response = requests.get("https://api.github.com")
print(response.status_code)
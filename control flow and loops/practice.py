#1.1
# num=int(input("enter the number"))
# print(num)
# if num > 0:
#     print("number is positive")
# elif num < 0:
#     print("numner is negative")
# else:
#     print("number is zero")     

#1.2

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote ")
# else:
#     print("You are NOT eligible to vote ")

#1.3

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

#2.1
# day = int(input("Enter a day number (1-7): "))

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid day number! Please enter between 1-7.")      

#2.2
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))


# op = input("Enter operation (+, -, *, /): ")

# match op:
#     case "+":
#         print("Result:", a + b)
#     case "-":
#         print("Result:", a - b)
#     case "*":
#         print("Result:", a * b)
#     case "/":
#         if b != 0:
#             print("Result:", a / b)
#         else:
#             print("Error! Division by zero is not allowed.")
#     case _:
#         print("Invalid operation! Please enter +, -, *, or /.")

#3.1
# for i in range(1,11):
#     print(i)
#3.2
# num = int(input("Enter a number: "))

# print(f"Multiplication Table of {num}:")
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")
#3.3
# total = 0

# for i in range(1, 101):
#     total += i
# print(f"{total} is the sum of numbers from 1 to 100")  
#3.4
# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")  
#     print()      

# password="Dolly"
# enter_pass =input("Enter Password ")

# while password!=enter_pass:
#     enter_pass=input("Wrong Password !!! Try Again ")

# print("Success! You have entered the Correct Password ")    

num=455533
print(int(str(num)[::-1]))
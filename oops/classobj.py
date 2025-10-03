# Classes and Objects: The Blueprint and the Building
# Class: Think of a class as a blueprint or a template. It defines what an object will be like – what data it will hold and what actions it can perform. It doesn't create the object itself, just the instructions for creating it. It's like an architectural plan for a house.

# Object (Instance): An object is a specific instance created from the class blueprint. If "Car" is the class, then your red Honda Civic is an object (an instance) of the "Car" class. Each object has its own unique set of data. It's like the actual house built from the architectural plan.

# class Employee:
#     company="Hp"
#     def get_salary(self):#self is important here because slef is the way to reference the object the class is being created 
#         print(self)
#         return 234

# e=Employee()
# print(e.get_salary())
# e2=Employee()
# print(e2.get_salary())
# Constructors in Python
# The Constructor: Setting Things Up (__init__)
# The __init__ method is special. It's called the constructor. It's automatically run whenever you create a new object from a class.

# What's it for? The constructor's job is to initialize the object's attributes – to give them their starting values. It sets up the initial state of the object.
class Employee:
    company="Hp"     
    def __init__(self,salary,name,bond,company):
        self.salary=salary
        self.name=name
        self.bond=bond
        self.company=company
    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"the name of the employee is {self.name} salary is {self.salary} and bond is for {self.bond} years")  
e=Employee(23400,"dolly",2)  
#print(e.get_salary())  
e.get_info()
print(e.company)

# Class vs. Instance Attributes:
# Class Attributes: These are shared by all objects of the class. Like species in our Dog class. All dogs belong to the same species. They are defined outside of any method, directly within the class.

# Instance Attributes: These are specific to each individual object. name and breed are instance attributes. Each dog has its own name and breed. They are usually defined within the __init__ method.

#object introspection


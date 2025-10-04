# Instance Methods: These are the most common type of method. They operate on instances of the class (objects) and have access to the instance's data through the self parameter.
# Class Methods: These methods are bound to the class itself, not to any particular instance. They have access to class-level attributes and can be used to modify the class state. They receive the class itself (conventionally named cls) as the first argument.
# Static Methods: These methods are associated with the class, but they don't have access to either the instance (self) or the class (cls). They are essentially regular functions that are logically grouped within a class for organizational purposes.

class Employee:
    company="Hp"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    #    instance method
    def get_info(self):
        print(f"the name of the employee is {self.name} salary is {self.salary}" ) 
    @staticmethod    
    def sum(a,b):
        return a+b
    @classmethod
    def print_company(cls):
        print(cls.company)

e1=Employee("Khil",9)
e1.get_info()
e2=Employee("Jhil",900) 
e2.get_info()     
print(e2.sum(6,8))
e1.print_company()
# Static methods are marked with the @staticmethod decorator. They are similar to regular functions, except they are defined within the scope of a class.

# They don't take self or cls as parameters.
# They are useful when a method is logically related to a class but doesn't need to access or modify the instance or class state.
# Often used for utility functions that are related to the class


# Instance methods are the most common type and operate on individual objects (self).
# Class methods operate on the class itself (cls) and are often used for factory methods or modifying class-level attributes.
# Static methods are utility functions within a class that don't depend on the instance or class state. They're like regular functions that are logically grouped with a class.
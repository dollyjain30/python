# In object-oriented programming, getters and setters are methods used to control access to an object's attributes (also known as properties or instance variables). They provide a way to encapsulate the internal representation of an object, allowing you to validate data, enforce constraints, and perform other operations when an attribute is accessed or modified. While Python doesn't have private variables in the same way as languages like Java, the convention is to use a leading underscore (_) to indicate that an attribute is intended for internal use.
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @property    
    def first_name(self):
        l=self.name.split(" ")
        #print(l)
        return l[0]   
    @first_name.setter 
    def first_name(self,first):
        l=self.name.split(" ")
        new_name=f"{first} {l[1]}"
        self.name=new_name
e = Employee("Jack do",344)
# e.projects=4
# print(e.first_name())
# e.set_first_name("Jan")
# print(e.name)
# print(e.projects);       
e.first_name="Jan"
print(e.name)


# Encapsulate data and enforce validation: You can check if the new value meets certain criteria before assigning it.
# Control access to "private" attributes: By convention, attributes starting with an underscore are considered private, and external code should use getters/setters instead of direct access.
# Make the code more maintainable: Changes to the internal representation of an object don't necessarily require changes to code that uses the object.
# Add additional logic: Logic can be added when getting or setting attributes.

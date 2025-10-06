# Inheritance is like a family tree. A child class (or subclass) inherits traits (attributes and methods) from its parent class (or superclass). This allows you to create new classes that are specialized versions of existing classes, without rewriting all the code.

class Animal:
    location ="Australia"
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("generic sound !!",self.name)
class Dog(Animal):
    def speak(self):
        super().speak()#we are using the speak function of the parent class 
        print("Woof!")
# a=Animal("Cow")
# a.speak()      
d=Dog("Jo")
d.speak()
# print(d.location)  

# Polymorphism: One Name, Many Forms
# Polymorphism, as we saw with the speak() method in the inheritance example, means that objects of different classes can respond to the same method call in their own specific way. This allows you to write code that can work with objects of different types without needing to know their exact class.
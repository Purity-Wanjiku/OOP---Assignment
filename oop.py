# OOP - It is a programming paradigm that organizes software design in objects as opposed to having functions an dlogic
# They have attributes and behaviour
# It can represent any real world objects that we are writing programs for.
# We define objects in python using classes.
# Classes define the attributes and methods/behaviour/functions
# Classes define an object ut does not actually create an object
#To create an object , you create an instance of that class


class Student:
    name = "Elizabeth"
    age =37
    school = "Akirachix"
    nationality = "kenya"
    
    #INSTANCE VARIABLE
    #WE CREATE A class where each instance of the clas has its own data
    #we use __init__ method  __init__(self,arguments)  self referring to the object instance of the class


class Students:
     school = "Akirachix"
     def __init__(self,name,age,nationality):
            self.name = name
            self.age=age
            self.nationality=nationality

    
#  INHERITANCE IN OOP
class Animal:
    def eat(self):
        print ("I can eat!")
    def sleep(self):
        print("I can sleep!")
        
class Dog(Animal):
    
    def bark(self):
        print ("I can bark! Woof! Woof!")
    def eat(self):
        print("I cannot eat everything")
        
# instances
dog1 = Dog()
dog1.eat()
dog1.bark()
dog1.sleep()

dog2 = Animal()
dog2.eat()

# Python Encapsulation
# Encapsulation refers to the bundling of attributes and methods inside a single class
# It prevents outer classes from accessing and changing attributes and methods of a class.

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
        #  The value of self.__maxprice is inserted into the string at the position of {}. 
        #  This allows the value to be displayed when the sell() method is called.

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# Here, we have tried to modify the value of __maxprice outside of the class. 
# However, since __maxprice is a private variable, this modification is not seen on the output.

# using setter function
c.setMaxPrice(1000)
c.sell()
# To change the value, we have to use a setter function i.e setMaxPrice() which takes price as a parameter.

# Polymorphism
# It simply means the same entity (method or operator or object) can perform different operations in different scenarios.

class Polygon:
    # method to render a shape
    def render(self):
        print("Rendering Polygon...")

class Square(Polygon):
    # renders Square
    def render(self):
        print("Rendering Square...")

class Circle(Polygon):
    # renders circle
    def render(self):
        print("Rendering Circle...")
    
# create an object of Square
s1 = Square()
s1.render()

# create an object of Circle
c1 = Circle()
c1.render()

# The main purpose of the render() method is to render the shape. 
# However, the process of rendering a square is different from the process of rendering a circle.
# the render() method behaves differently in different classes. 
# Or, we can say render() is polymorphic.




# Principles of OOP (Inheritance, Encapsulation,Polymorphism)
# Importance of the principles of OOP
  # Data is safe and secure with data abstraction - It refers to the process of hiding the implementation details of data structures 
     # and exposing only the essential attributes and behaviors of an object or data type.
     # Data abstraction allows for encapsulation
     # Only the necessary methods and attributes are exposed, ensuring that data is accessed and modified only through controlled and defined interfaces.
     # Data abstraction allows for information hiding, which means that the internal details of data are not accessible to external entities.
  # Since the class is sharable, the code can be reused.
  # OOP makes the program easy to understand as well as efficient
  # Polymorphism allows the same interface for different objects. Makes code efficient
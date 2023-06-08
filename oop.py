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

    
    

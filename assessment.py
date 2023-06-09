# QStn 1.
# The Ever-changing Ankara: 
# You are a fashion designer known for your unique and vibrant Ankara designs. 
# Recently, you've discovered that some of your fabric patterns change their designs based on 
# the temperature and mood of the wearer. 
# You want to create a software application that can predict the changes in the fabric design 
# given the mood and temperature data. 
# Think about the classes you will need to model the changing Ankara 
# and how to predict the changes

class AnkaraDesign:
    def __init__(self,temp,mood):
        self.temp = temp
        self.mood = mood
    
    def predict_changes(self):
        temps = 37
        if self.mood == "happy":
            if self.temp > temps:
                return "Ankara design changes to polkadots"
            if self.temp <temps:
                return "Ankara design changes to checked boxes"
        if self.mood == "sad":
            if self.temp > temps:
                return "Ankara design changes to straight lines"
            if self.temp <temps:
                return "Ankara design changes to wavy"
        else:
            return "Ankara does not change design"
        
design1 = AnkaraDesign(37,"happy")
design2 = AnkaraDesign(7,"sad")
design3 = AnkaraDesign(40,"happy")

print (design1.predict_changes())
print (design2.predict_changes())
print (design3.predict_changes())



# Qstn. 2
# The Magical Baobab: 
# In a small village, there is a Baobab tree believed to have magical properties. 
# Every season, it bears different types of fruits, each with its own unique power. 
# You've decided to create a software system that tracks the changes in the tree 
# and predicts what type of fruit it will bear next season and what powers it will possess.
# The system should also record the effect of each fruit when consumed
empty_list =[]
class Possible_Fruit:
    def __init__(self,powers,effect,season,name):
        self.powers=powers
        self.effect=effect
        self.season=season
        self.name=name
    def __repr__(self):
         return f"{self.name} {self.effect} {self.powers} {self.season}"
fruits = Possible_Fruit(powers="changecolor",effect="gives energy",season="wet",name="big baobab")
empty_list.append(fruits)
print(fruits)
print(empty_list)
class Seasons:
    def __init__(self,seasons):
        self.seasons = seasons
    def __str__(self):
            return f"{self.seasons}"
    def predict_fruit(self):
        for item in empty_list:
            if self.seasons == item.season:
                print( f"{item.name} was produced in the {self.seasons} season")
s = Seasons(seasons="wet")
s.predict_fruit()

# Qstn3.
# Nollywood Movie Planner: 
# As a producer in the booming Nollywood movie industry, 
# you are in charge of multiple film projects at once. 
# Each movie has different cast members, shooting schedules, and budgets.
# You want to write a program to help manage your film projects efficiently. 
# The software should be able to handle the complexities of scheduling, budgeting, 
# and coordinating between different movie projects.


# Qstn4.
# The Magical Baobab: 
# In a small village, there is a Baobab tree believed to have magical properties. 
# Every season, it bears different types of fruits, each with its own unique power. 
# You've decided to create a software system that tracks the changes in the tree 
# and predicts what type of fruit it will bear next season and what powers it will possess. 
# The system should also record the effect of each fruit when consumed

# Qstn 5.
# The Legendary African Drum Circles:
# You're part of a community that hosts one of the largest drum circles in Africa. 
# There are different types of traditional drums used in the circle, 
# each with its unique sound and rhythm. The Djembe, Talking Drum, and Bougarabou 
# are among the popular ones. These drums have common properties such as 
# the material they're made from and their sizes, but they also have distinct characteristics. 
# For instance, the Talking Drum can mimic the lines of human speech, 
# the Djembe is known for its wide range of tones, and the Bougarabou is noted for its deep, rich bass tones.
# You want to create a software model of the drum circle that encapsulates these different types of drums. 
# You wish to include methods for each drum that represent the sound it makes, and also group similar drums together.
# Think about creating a base Drum class that contains properties and methods common to all drums, 
# and then create subclasses for each specific type of drum (like Djembe, Talking Drum, and Bougarabou).
# The subclasses should inherit from the base Drum class and also implement their unique characteristics. 
# This software model would help newcomers understand the characteristics of each drum 
# and how they contribute to the overall rhythm of the drum circle. 

class Drum:
    def __init__(self,material,size):
        self.material=material
        self.size=size
    def makeSound(self,tones):
        print(f"The drum makes {tones}")
class Djembe(Drum):
    def makeSound(self,tones):
        print(f"The Djembe drum makes {tones}")
class TalkingDrum(Drum):
    def makeSound(self,tones):
        print(f"The drum makes {tones}")
class Bougarobou(Drum):
    def makeSound(self,tones):
        print(f"The Bougarabou drum makes {tones}")
        
drum=Drum("wood","large")
drum.makeSound("du du du")
djembe=Djembe("leather","medium")
print (djembe.material)
djembe.makeSound("High,medium,low")
talkingDrum=TalkingDrum("plastic","small")
talkingDrum.makeSound("Mimics human speech")
bougarabou=Bougarobou("synthetic fibre","extra large")
bougarabou.makeSound("rich bass")

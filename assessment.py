# QStn 1.
# The Ever-changing Ankara: 
# You are a fashion designer known for your unique and vibrant Ankara designs. 
# Recently, you've discovered that some of your fabric patterns change their designs based on 
# the temperature and mood of the wearer. 
# You want to create a software application that can predict the changes in the fabric design 
# given the mood and temperature data. 
# Think about the classes you will need to model the changing Ankara 
# and how to predict the changes



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

#They add behaviour to classes hence operate on the class attribute
#we use normal python functions
class Students:
     school = "Akirachix"
     def __init__(self,name,age,nationality):
            self.name = name
            self.age=age
            self.nationality=nationality
     def greet_student (self):
         return f" Hello {self.name}. Welcome to {self.school}"
     
     def year_of_birth(self):
         year = 2023 - self.age
         return f"Hello {self.name}. You wre born in {year}"
     
class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
        
    def match_animal_sound(self):
        return f"Name: {self.name},Sound:{self.sound}"
        
my_pet = Animal("cat","meow")
info=my_pet.match_animal_sound()
print(info)


class Restaurant:
    def __init__(self,total_tables):
        self.total_tables = total_tables
        
    def occupy_tables(self,occuppied_tables):
        self.total_tables -= occuppied_tables
        print(self.total_tables)
         
    def reserve_tables(self, reserved_tables):
     if reserved_tables < 2:
         return "The number of tables to reserve must be at least 2."
    # Check if there are enough available tables
     if self.total_tables < reserved_tables:
         return "There are not enough available tables."
    # Reserve the tables
     self.total_tables -= reserved_tables
     return f"User has reserved {reserved_tables} tables for the night, and {self.total_tables} table(s) are left"
    #  return self.total_tables
        
maathe = Restaurant(24)
maathe.occupy_tables(21)
x = maathe.reserve_tables(5)
print (x)

              
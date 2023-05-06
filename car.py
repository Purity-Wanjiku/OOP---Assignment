class Car:
    wheels=4
    def __init__(self,make,model,color):
     self.make = make
     self.model = model
     self.color = color
    def start_car(self):
        return "vroom vroom"
    def car_capacity(self):
        return f"My {self.make} has {self.wheels} wheels and can carry 1 person"
    def car_speed(self):
        return f"The {self.model} VX can move at a speed of 24km/hr"
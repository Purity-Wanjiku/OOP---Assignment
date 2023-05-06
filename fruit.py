class Fruit:
    nutrients="Vitamin c"
    def __init__ (self,type,name,color):
        self.type=type
        self.name=name
        self.color=color
    def fruit_describe(self):
        return f"These {self.type} are like {self.name}"
    def fruit_sort(self):
        return f"These {self.name} are of color {self.color}"
    def fruit_expiry_date(self,date):
        date_is=date
        return  f"Fruits with {self.nutrients} expire by {date_is}"
    
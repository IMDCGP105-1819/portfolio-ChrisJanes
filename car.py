class Car(object):

    def __init__(self, colour, manufacturer, model, doors):
        self.colour = colour
        self.manufacturer = manufacturer
        self.model = model
        self.doors = doors
    
    def change_colour(self, colour):
        self.colour = colour  

    def __str__(self):
        return f"{self.colour.title()} {self.manufacturer.title()} {self.model.title()} with {self.doors!s} doors"

car = Car("blue", "Ford", "Fiesta", 3)
print(car)
from food import Meat
from animals.animal import Bird
class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"
    
    def feed(self, food):
        if not isinstance(food, Meat):
            return f"Owl does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.25
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"Owl [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
    
class Hen(Bird):
    def make_sound(self):
        return "Cluck"
    
    def feed(self, food):
        self.weight += food.quantity * 0.35
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"Owl [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
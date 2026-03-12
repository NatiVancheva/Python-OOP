from food import Vegetable, Fruit, Meat
from animals.animal import Mammal
class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"
    
    def feed(self, food):
        if not isinstance(food, Vegetable, Fruit):
            return f"Mouse does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.10
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"Mouse [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
    
class Dog(Mammal):
    def make_sound(self):
        return "Woof"
    
    def feed(self, food):
        if not isinstance(food, Meat):
            return f"Mouse does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.40
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"Mouse [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
    
class Cat(Mammal):
    def make_sound(self):
        return "Meow"
    
    def feed(self, food):
        if not isinstance(food, Vegetable, Meat):
            return f"Mouse does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.30
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"Mouse [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
    
class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"
    
    def feed(self, food):
        if not isinstance(food, Meat):
            return f"Mouse does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 1
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"Mouse [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
    
       
from project.animal import Animal
class Tiger(Animal):
    MONRY_FOR_CARE = 45
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender, Tiger.MONRY_FOR_CARE)
      
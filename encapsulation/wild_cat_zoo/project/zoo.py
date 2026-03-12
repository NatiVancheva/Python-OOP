from project.caretaker import Caretaker

from project.cheetah import Cheetah

from project.keeper import Keeper

from project.lion import Lion

from project.tiger import Tiger

from project.vet import Vet

class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        animal_type = animal.__class__.__name__
        if len(self.animals) < self.__animal_capacity:
            if self.__budget > price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal_type} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"
    
    def hire_worker(self, worker):
        worker_type = worker.__class__.__name__
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker_type} hired successfully"
        return "Not enough space for worker"
    
    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"
    
    def pay_workers(self):
        salaries = sum(worker.salary for worker in self.workers)
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_care = sum(animal.money_for_care for animal in self.animals)
        if self.__budget >= money_care:
            self.__budget -= money_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."
    
    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        tigers = [animal for animal in self.animals if isinstance(animal, Tiger)]
        lions = [animal for animal in self.animals if isinstance(animal, Lion)]
        cheetahs = [animal for animal in self.animals if isinstance(animal, Cheetah)]

        result = [f"You have {len(self.animals)} animals"]

        result.append(f"- - - - - {len(lions)} Lions: ")
        for lion in lions:
            result.append(repr(lion))
        
        result.append(f"- - - - - {len(tigers)} Tigers: ")
        for tiger in tigers:
            result.append(repr(tiger))

        result.append(f"- - - - - {len(cheetahs)} Cheetahs: ")
        for cheetah in cheetahs:
            result.append(repr(cheetah))

        return "\n".join(result)
    
    def workers_status(self):
        keepers = [worker for worker in self.workers if isinstance(worker, Keeper)]
        caretakers = [worker for worker in self.workers if isinstance(worker, Caretaker)]
        vets = [worker for worker in self.workers if isinstance(worker, Vet)]

        result = [f"You have {len(self.workers)} workers"]

        result.append(f"- - - - - {len(keepers)} Keepers: ")
        for keeper in keepers:
            result.append(repr(keeper))
        
        result.append(f"- - - - - {len(caretakers)} Caretakers: ")
        for caretaker in caretakers:
            result.append(repr(caretaker))

        result.append(f"- - - - - {len(vets)} Vets: ")
        for vet in vets:
            result.append(repr(vet))

        return "\n".join(result) 
        
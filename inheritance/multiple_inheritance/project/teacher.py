from project.person import Person
from project.employee import Employee
class Teacher(Person, Employee):
    def teach():
        return "teaching..."
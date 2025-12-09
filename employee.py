# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
    
    @abstractmethod
    def calculate_bonus(self):
       pass
        
    def display_emp_detials(self):
        print("Employeee Name", self.name, "Base Salary: ", self.salary)
        
class Developer(Employee):
    def calculate_bonus(self):
        bonus = (10 / 100) * self.salary
        print("Bonus:", bonus)
        return bonus
    def display_emp_detials(self):
        print("Employeee Name", self.name, "Base Salary: ", self.salary, "as a Developer")   
    
class SeniorDev(Developer):
    def calculate_bonus(self):
        bonus = 0.02 * self.salary
        print("Bonus:", bonus)
        return bonus
        
    def display_emp_detials(self):
        print("Employeee Name", self.name, "Base Salary: ", self.salary, "as a Senior Developer")   
        
objEmp = Developer("A",10000)
objSen = SeniorDev("B",10000)
objSen.display_emp_detials()
objEmp.display_emp_detials()
objEmp.calculate_bonus()
objSen.calculate_bonus()


    

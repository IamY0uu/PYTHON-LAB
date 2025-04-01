# write a class and add salary increment properties to it, use property decorator with a setter.
class Employee:
    def __init__(self):
        self.salary = 2000
        self.increment = 15 

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * (self.increment / 100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):  
        self.increment = ((new_salary / self.salary) - 1) * 100

e = Employee()
e.salaryAfterIncrement = 4000  
print(e.increment)  

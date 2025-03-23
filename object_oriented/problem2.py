#  create a class which can give Square, SquareRoot, Cube of a number
class Calculator:
    def __init__(self, num):
        self.num = num  # Instance variable
    
    def square(self):
        return self.num * self.num
        
    def squareRoot(self):
        return round(self.num ** 0.5, 2)
        
    def cube(self):
        return self.num * self.num * self.num
    

num = int(input("Enter a number: ")) # User input
obj = Calculator(num)  # Object creation


print("Square:", obj.square())  
print("Square Root:", obj.squareRoot())  
print("Cube:", obj.cube())  


# make a class to represent COMPLEX NUMBERS , along with overloaded operators '+' and '*'.
class complex:
    def __init__(self,i,r):
        self.r = r
        self.i = i
        
    def __add__(self,other):
        return complex(self.r + other.r, self.i + other.i)
    
    def __mul__(self, other):
        real_part = self.r * other.r - self.i * other.i
        imag_part = self.r * other.i + self.i * other.r
        return complex(real_part, imag_part)
     
    def __str__(self):
        return f"{self.r} + {self.i}j"
    
    
obj = complex(3,4)
obj2 = complex(1,2)
     
print("addition: ",obj + obj2)
print("multiplication: ",obj * obj2)

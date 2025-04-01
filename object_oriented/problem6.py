# concept of multi levele inheritence.
class animals:
    print("This is animal class.")
class pets(animals):
    print("This is pets class.")
class dog(pets):
    def bark(self,name):
        self.name = name
        print(f"This is dog class, {self.name}")
        
obj= dog()
obj.bark("harry")
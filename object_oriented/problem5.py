# concept- inheritence, store 2D & 3D vector's coordinates.
class TwoDvector:
    def two(self,x,y):
        self.x = x
        self.y = y
        print("\nThis is 2D-Vector.")
        print(f"Coordinates are {self.x}, {self.y} ")
        
class ThreeDvector(TwoDvector):
    def three(self,z):
        self.z = z
        print("\nThis is 3D-vector.")
        print(f"Coordinates are {self.x}, {self.y}, {self.z}\n")
        
obj = ThreeDvector()
obj.two(45,55)
obj.three(23)


class parent1:
    name = "Rakesh"
    def p1(self):
        print(f"\nThis is Parent1 class. It have {self.name}.")
        
class parent2(parent1):
    company="Microsoft"
    def p2(self):
        print(f"\nThis is Parent2 class. It have {self.company}.")
        
class child(parent2):
        def class_method(self):
            print("\nThis is child / inherited class.")
            print(f"It fetches {self.name}, {self.company} from Parent classes.\n")
        
        
object = child()
object.p1()
object.p2()
object.class_method()
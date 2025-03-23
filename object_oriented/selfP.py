class employee:
    language= "python"  #class attribute
    salary= 1200000 #class attribute
    
    def getInfo(self): #normal function
        print(f"\nemployee salary: {self.salary} \nlanguage is: {self.language}")
        
        
    def greet(self):     # self parametere likhne ka matlab h is function mein "object" use honge
        print("\nfunction with self parameter")
        
       
    @staticmethod    # agar self nai likhna to " @staticmethod " likho , matlab function mein 'object' use nai hoga
    def meet():
        print("\nfunction without self parameter")


    def __init__(self, name, salary, language): # starts with underscore (_) , automatically called
        print("\nThis is dunder method")
        self.name = name
        self.salary = salary
        self.language = language
        


harry = employee("garry", 1500000, "java")
# harry.name = "harry"    #object / instance attribute
print(harry.name, harry.salary, harry.language)

## dono same he hai
# harry.getInfo()
# employee.getInfo(harry)

## with self / without self
# harry.greet() 
# harry.meet()

# def avg():
#     a=int(input("num1: "))
#     b=int(input("num2: "))
#     c=int(input("num3: "))
#     avg=(a+b+c)/3
#     print(avg)
# avg()
# def greet(name, end):
#     # print("have a nice day "+ name)
#     # print(end)
#     return name

# a = greet("ajay","gupta")
# print(a)

def greet(name="Guest"):  # Default value "Guest" set ki
    print(f"Hello, {name}!")

greet("Hemant")  # Argument diya -> name = "Hemant"
greet()  # Koi argument nahi diya -> name = "Guest"

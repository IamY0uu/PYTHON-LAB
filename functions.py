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

# def factorial(n):  # Default value "Guest" set ki
#     if(n==1 or n==0):
#         return 1
#     return n * factorial(n-1)
# n=int(input("Num:"))
# print(f"factorial of num= {factorial(n)}")


# def gt():
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#         return c

# a=int(input("a: "))
# b=int(input("b: "))
# c=int(input("c: "))
# print(f"{gt()} is greatest")

#  c=5*(f-32)/9


# def stars(n):
#     for i in range(n,0,-1):
#         print("*"*i)
# n=int(input("num: "))
# stars(n)


# inches to cm
# def func(inc):
#     cm = inc * 2.54
#     return cm
# inc=int(input("inches: "))
# print(f"{func(inc)} cm")



# use of strip 
# def func(words, remove_word):
#     cleaned_list = [word.replace(remove_word, "").strip() for word in words]
#     return cleaned_list
# words = ["  apple pie", "banana", "apple juice  ", " mango  "]
# remove_word = "apple"
# print(func(words, remove_word))



# func for table 
# def table(n):
#     for i in range (1,11,1):
#          ans = n*i
#          print (f"{n} x {i} = {ans}")
# n=int(input("num: ")) 
# table(n)


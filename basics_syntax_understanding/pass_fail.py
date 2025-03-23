a=int(input("enter sub1: "))
b=int(input("enter sub2: "))
c=int(input("enter sub3: "))

tp= (a+b+c)/3
if(tp>=40):
    print("you've passed !!")
else:
    print("you've failed !!")
    
if (a<33):
    print("and you,ve failed in sub1")
elif (b<33):
    print("and you,ve failed in sub2")
elif (c<33):
    print("and you,ve failed in sub3")
else:
    print("you've passed in all subjects")
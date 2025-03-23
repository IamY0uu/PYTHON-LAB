class employee:
    lang= "python"  #class attribute
    salary= 1200000 #class attribute

harry = employee()
harry.name = "harry"    #object / instance attribute
print(f"\n{harry.name}\n{harry.lang} \n{harry.salary}")

rohan = employee()
rohan.name = "rohan"     #object / instance attribute
print(f"\n{rohan.name}\n{rohan.lang} \n{rohan.salary}")

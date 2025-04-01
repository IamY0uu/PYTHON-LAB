# create a class , set a class attribute 'a' , create a object and set 'a' using object.a = 0
# now check if class attribute changes.

class attribute:
    a = 12
    
object = attribute()
print(object.a) #class attribute is printed , bcz instance attribute not set
object.a=0      #instance attribute is set
print(object.a) #will print instance attribute, due to higher preference

# NO, class attributes doesn't change instead it gets overriden by instance attributes
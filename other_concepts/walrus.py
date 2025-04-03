# Using walrus operator.
if(n:= len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)") 
    
    
    
# no need to write in usual syntax, if you use walrus(:=) operator.
# n = [1,2,3,4,5]
# if len(n) > 3:
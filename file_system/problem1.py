# check occurrence of a word in a file 
with open("poems.txt") as f:
   content = f.read()
if "twinkle" in content:
    print("yes")
else:
    print("no")
# check if files (this.txt and copy.txt) are identical or not
with open("this.txt") as f:
    main = f.read()
with open("copy.txt") as f:
    copy=f.read()
    
if copy == main:
    print(True)
else:
    print(False)
    
    
## to wipe content of a file
# with open("copy.txt","w") as f:
#     f.write("")

## to rename a file 
# simply put content in another file with new name 

## to remove a file 
# import os
# file_path = "sample.txt"  
# if os.path.exists(file_path):
#     os.remove(file_path)
#     print(f"{file_path} deleted successfully!")
# else:
#     print("File not found!")

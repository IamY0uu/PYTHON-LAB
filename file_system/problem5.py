# read a log file and check if it has python
with open("log.txt") as f:
    lines = f.readlines()
    lineno = 1
    for line in lines:
        if "python" in line:
            print(f"yes in line: {lineno}")
            break
        lineno +=1 
    else:
        print("no")
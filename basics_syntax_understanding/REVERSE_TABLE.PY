n=int(input("n: "))
table=[]
for i in range(1,11):
    table.append((f"{n}x{11- i}={n* (11-i)}"))
table.reverse()
for item in table:
    print(item)
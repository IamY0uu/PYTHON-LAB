try:
    a = int(input("a: "))
    print(a)
except Exception as e:
    print(e)
    print("Program didn't crash , it prints error.")
import random
dict={
        "snake" : -1,
        "water" : 0,
        "gun" : 1,
}
print(f"options : {list(dict.keys())}")

while True:
    user= input("user choice: ").strip().lower()
    if user in dict:
        user=dict[user]
        break
    else:
         print("Invalid choice!!")
         
         
computer=random.choice(list(dict.keys()))
print(f"computer choice: {computer}")
computer=dict[computer]

if (computer==-1 and user==1) or (computer==0 and user==-1) or (computer==1 and user==0):
    print("You win!!")
elif (computer==user):
    print("draw!!")
else:
    print("you lose!!")


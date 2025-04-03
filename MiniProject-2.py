# The Perfect Guess
import random
number = random.randint(1,1000)
guess = 0
guesses = 1

while number != guess:
    
    guess = int(input("your guess: "))
    
    if guess > number:
        print("Lower number please")
    else:
        print("Greater number please")
        break
    guesses += 1
    
print("BINGO !!")
print("Total guesses: ",guesses)
# game which generates highscore, and stores it in a file (highscore.txt) .
import random
def game():
    print("you're playing the game")
    score = random.randint(1, 62)
    
    with open("highscore.txt") as f:
            highscore = f.read()
            if (highscore != ""):
                highscore = int(highscore)
            else:
                highscore = 0
    print(f"high score: {score}")
            
    if (score>highscore):
        with open("highscore.txt", "w") as f:
            f.write(str(score))

    return score

game()

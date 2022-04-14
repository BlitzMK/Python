#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)
#Extras:
#Keep the game going until the user types “exit”
# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random as rd

target = rd.randint(1,9)

def guess(max,min):
    inp = input("Enter a guess between "+ str(min) + " and " + str(max) + ": ").lower()
    if(inp == "exit"):
        return inp
    elif(int(inp) > max or int(inp) < min):
        print("out of range")
        inp = guess(max, min)
    return inp



a = 1
b = 9

while True:
    g = guess(b,a)
    if(g == "exit"):
        break
    elif(int(g) == target):
        print("You got it!")
        Cont = input("Play Again? ").lower()
        if(Cont == 'no' or Cont == 'exit'):
            break
        target = rd.randint(1,9)
    elif(int(g) > target):
        print("To high")
    else:
        print("To low")


# Create a program that will play the “cows and bulls” game with the user. 
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
# For every digit that the user guessed correctly in the correct place, they have a “cow”. 
# For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
# Once the user guesses the correct number, the game is over. 
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

# https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html

import random as rd

def getUserInput():
    guess = input("enter a 4 digit number (ex 1234): " ).strip(" ")

    while(len(guess) != 4):
        print("invalid input must be only 4 digits")
        guess = input("enter a 4 digit number (ex 1234): " )
        

    return list(guess)


# declaring viables
cow = 0
bull = 0
guess = ""
guessAmount = 0
win = False
i = 0
answer = rd.sample(range(0,10),4)
# print(answer)



print("Welcome to Cows and Bull Game")

while(win == False):
    guess = getUserInput()
    guessAmount += 1
    # print("".join(guess))

    for x in guess:
        if int(x) == int(answer[i]):
            cow += 1
            bull -= 1
        for y in answer:
            if int(x) == int(y):
                bull += 1
        i += 1
    print("Bulls: "+ str(bull) + "   Cows: "+ str(cow))

    i = 0

    if(cow == 4):
        win = True
        print("Congrats you win\nGuesses: " + str(guessAmount))

    cow = 0
    bull = 0


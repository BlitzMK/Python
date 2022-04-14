# Make a two-player Rock-Paper-Scissors game. 
# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
print("Welcome to RPS choose 'R' Rock, 'P' Paper, and 'S' Scizzors")

def inp():
    while True:
        p1 = input("Player 1: ")
        p1 = p1[0].lower()
        if(p1 == 'r' or p1 == 'p' or p1 == 's'):
            break
        else:
            print("Invalid input")


    while True:
        p2 = input("Player 2: ")
        p2 = p2[0].lower()
        if(p2 == 'r' or p2 == 'p' or p2 == 's'):
            break
        else:
            print("Invalid input")

    return p1,p2

def playAgain():
    while True:
        result = input("Play Again (yes or no) ? ")
        if(result == 'yes'):
            return True
        elif(result == 'no'):
            return False
        else:
            print("Invalid Input")
        


P1Score = 0
P2Score = 0

in1,in2 = inp()

if(in1 == in2):
    print("Draw")
elif((in1 == "p" and in2 == "r") or (in1 == "r" and in2 == "s") or (in1 == "s" and in2 == "p")):
    print("Player 1 Wins")
    P1Score = P1Score +1
else:
    print("Player 2 Wins")
    P2Score = P2Score +1
print("Score:\nPlayer 1: "+str(P1Score)+"  \nPlayer 2: "+ str(P2Score))

while playAgain():

    in1,in2 = inp()
    if(in1 == in2):
        print("Draw")
    elif((in1 == "p" and in2 == "r") or (in1 == "r" and in2 == "s") or (in1 == "s" and in2 == "p")):
        print("Player 1 Wins")
        P1Score = P1Score +1
    else:
        print("Player 2 Wins")
        P2Score = P2Score +1
    print("Score:\nPlayer 1: "+str(P1Score)+"  \nPlayer 2: "+ str(P2Score))
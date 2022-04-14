# Write a password generator in Python. 
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
# https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
import random as rd




def GeneratePassword():
    # get password strength
    strength = int(input("enter the stength of the password(1-10): "))
    while(strength > 10 and strength < 1):
        strength = int(input("enter the stength of the password(1-10): "))

    # defining variables to construct password list 
    Words = ["beatle", "canoe", "owl", "cloud", "tiger", "second", "once", "third", "snake", "robot"] # list of words
    num = ["0","1","2","3","4","5","6","7","8","9"] # list of numbers
    punct = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "?"] # a list of punctuations
    password = list()

    # streagth = 1, just a word 
    password.append(rd.choice(Words))

    # strength = 2, add a number + shuffle contents
    if(strength >=2):
        password.append(rd.choice(num)) 
        rd.shuffle(password)

    # strength = 3, add a punctuation + shuffle contents
    if(strength >=3):
        password.append(rd.choice(punct))
        rd.shuffle(password)
    # strength = 4, add a second word + shuffle contents
    if(strength >=4):
        password.append(rd.choice(Words))
        rd.shuffle(password)

    # strength = 5, add a number + shuffle contents
    if(strength >=5):
        password.append(rd.choice(num))
        rd.shuffle(password)

    # strength = 6, add a word + shuffle contents
    if(strength >=6):
        password.append(rd.choice(Words))
        rd.shuffle(password)

    # strength = 7, random caps + shuffle contents
    if(strength >=7):
        result=""
        for c in "".join(password):
            case = rd.randint(0,1)
            if case == 0:
                result += c.lower()
            else:
                result += c.upper()
        password = list(result)
        rd.shuffle(password)


    # strength = 8, add 3 more numbers
    if(strength >=8):
        password.append(rd.choice(num))
        password.append(rd.choice(num))
        password.append(rd.choice(num))
        rd.shuffle(password)

    # strength = 9, add 3 more special characters
    if(strength >=9):
        password.append(rd.choice(punct))
        password.append(rd.choice(punct))
        password.append(rd.choice(punct))
        rd.shuffle(password)

    # strength = 10, password becomes password
    if(strength >=10):
        password = list("password")


    return "".join(password)

print(GeneratePassword())
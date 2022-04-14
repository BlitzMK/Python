# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Samuel Chandler 4/5/2022
# ex2: Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user.

divend = int(input("Enter Dividend: "))
divsor = int(input("Enter Divisor: "))
if(divend%divsor == 0):
    print(str(divend) +" and "+str(divsor) + " are divisable")
else:
    print(str(divend) +" and "+str(divsor) +  " are not divisable")
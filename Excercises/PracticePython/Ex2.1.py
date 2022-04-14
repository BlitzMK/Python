# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Samuel Chandler 4/5/2022
# ex1: If the number is a multiple of 4, print out a different message.

num = int(input("Enter a number: "))
if(num%4 == 0):
    print(str(num)+ " is divisable by four")
elif(num%2 == 0):
    print(str(num) + " is a even number. ")
else:
    print(str(num) + " is an odd number. ")
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Samuel Chandler 4/5/2022

num = int(input("Enter a number: "))

if(num%2 == 0):
    print(str(num) + " is a even number. ")
else:
    print(str(num) + " is an odd number. ")
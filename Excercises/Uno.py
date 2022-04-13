# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Samuel Chandler 4/5/2022

import datetime

baseyear = datetime.datetime.today().year
name = input("Enter Name: ")
age = input("Enter Age: ")
age = int(age)

deathYear= baseyear +100 - age

print(name + " you will die in year "+ str(deathYear) +".")

# can also be done with age = int(input("Enter Age: "))
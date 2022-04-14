# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.



def Fibonnaci(x):
    # x = number of numbers to generate
    result = [1,1]

    if(x == 0):
        return "none"
    elif(x==1):
        return [1]

    while(len(result) < x ):
        result.append(result[len(result)-1] + result[len(result)-2])

    return result

x = int(input())
print(Fibonnaci(x))
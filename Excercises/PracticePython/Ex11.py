# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
# Ask the user for a number and determine whether the number is prime or not.
#  (For those who have forgotten, a prime number is a number that has no divisors.). 

def prime(x):
    y = range(2,x-1)

    for a in y:
       if (x%a == 0):
            return False
    
    return True

inp = int(input("Enter a number: "))

if(prime(inp)):
    print("This number is prime")
else:
    print("This number is not prime")
# https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes. 
# Write this in one line of Python using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).

import random as rd

A = rd.sample(range(1,100), 20)
B = rd.sample(range(1,100), 10)

result = [a for a in A for b in B if a == b]

print(A)
print(B)
print(result)
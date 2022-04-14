# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# Extras:
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

import random as rd

def RemoveDuplicates(x):
    result = set()
    for i in x :
        result.add(i)

    return result

inp = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 21, 55]
print(RemoveDuplicates(inp))
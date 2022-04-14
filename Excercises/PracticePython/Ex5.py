# write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
#  Make sure your program works on two lists of different sizes.
#Randomly generate two lists to test this

import random as rd

# rd.sample(range 1 - 100, 10 elements in list )

A = rd.sample(range(1,100), 20)
B = rd.sample(range(1,100), 15)
result = []

for a in A:
    for b in B:
        if(a == b):
            result.append(a)

print(result)
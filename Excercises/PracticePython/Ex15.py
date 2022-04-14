# https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

inp = input("Enter a string to be reversed: ")

splitResult = inp.split()

result = splitResult[::-1]

result = " ".join(result)

print(result)


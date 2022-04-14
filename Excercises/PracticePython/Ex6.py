# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

x = input("Enter a String: ")
palandrome = True

#x[start:end:direction and incroment ammount]
if x == x[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
# print(x)
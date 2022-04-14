# write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
sentinel = int(input("Enter a max value: "))
b = []
for x in a:
    if(x < sentinel):
        b.append(x)

print(b)


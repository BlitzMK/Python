#  Print a list of all possible coordinates given by (i,j,k) 
#  on a 3D grid where the sum of i + j + k is not equal to n. 
# Here, 0<=i<=x, 0<=j<=y, 0<=j<=z . 
# Please use list comprehensions rather than multiple loops, as a learning exercise.
# https://www.hackerrank.com/dashboard



if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    lst = [ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(lst)
    


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max = -101
    second = -102
    y = -101
    for x in arr:
        if x > max:
            max = x
        elif x > second and x != max:
            second = x
        if y > second and y != max:
            second = y
        y = x
    print(str(second))  

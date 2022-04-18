if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple()
    for x in integer_list:
        t = t + (int(x),)
    print(hash(t))

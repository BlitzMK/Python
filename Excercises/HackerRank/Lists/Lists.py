


if __name__ == '__main__':
    N = int(input())
    l = []
    e = 0
    i = 0

    for x in range(N):
        full = input().split(" ")
        command = full[0]
        values = full[1:]

        if(command == "insert"):
            i = int(values[0])
            e = int(values[1])
            l.insert(i,e)
        elif command == "print" :
            print(l)
        elif command =="remove":
            e = int(values[0])
            l.remove(e)
        elif command == "append":
            e = int(values[0])
            l.append(e)
        elif command == "sort" :
            l.sort()
        elif command == "pop" :
            l.pop()
        elif command == "reverse":
            l.reverse()


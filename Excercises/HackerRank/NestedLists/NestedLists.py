from sys import last_traceback


if __name__ == '__main__':

    Last = [[101,float(101)]]
    second = []
    
    Students = []
    currentStudent = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        currentStudent = [name,score]
        Students.append(currentStudent)
        if currentStudent[1] < Last[0][1]:
            second = Last
            Last = currentStudent
        if currentStudent[1] == Last[0][1]:
            Last.append[currentStudent]
        
        print(second)
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    total =0
    average = 0
    num = 0 

    for i in student_marks[query_name]:
        total += i
        num += 1
    average = total/num
    print("%.2f"%(average))
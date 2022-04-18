
if __name__ == '__main__':

    second = 0 
    second_names = []
    Students = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Students.append([name,score])
        scores.add(score)
        
    second = sorted(scores)[1]

    for name,score in Students:
        if score == second: 
            second_names.append(name)
    
    for name in sorted(second_names):
        print(name, end = '\n')
        
        
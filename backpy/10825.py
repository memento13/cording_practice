import sys

n = int(sys.stdin.readline())
students = list()
for _ in range(n):
    temp_student = list(sys.stdin.readline().strip().split())
    for i in range(1,4):
        temp_student[i] = int(temp_student[i])
    students.append(temp_student)

result = sorted(students,key=lambda x: (-x[1],x[2],-x[3],x[0]))
for i in result:
    print(i[0])
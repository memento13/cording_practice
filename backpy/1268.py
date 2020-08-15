import sys

N = int(sys.stdin.readline())
students=[]
same = [-1]*N
for _ in range(N):
    students.append(list(map(int,sys.stdin.readline().strip().split())))

for i in range(N): #학생
    for j in range(N): #다른학생
        for k in range(5): #학년
            if students[i][k] == students[j][k]:
                same[i] += 1
                break

print(same.index(max(same))+1)

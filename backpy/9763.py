import sys

n = int(sys.stdin.readline())
town = []
for _ in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    town.append(temp)



def func(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])

result = func(town[0],town[1])+func(town[1],town[2])

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            temp = func(town[i],town[j])+func(town[j],town[k])
            result = min(temp,result)
print(result)
import sys

n = int(sys.stdin.readline())
condo = []
result = 0
for _ in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    condo.append(temp)

for i in condo:
    flag = True
    for j in condo:
        if i==j:
            continue
        if i[0]>j[0]:
            if i[1]>=j[1]:
                flag = False
                break
        elif i[1]>j[1]:
            if i[0]>=j[0]:
                flag = False
                break
    if flag:
        result+=1
print(result)
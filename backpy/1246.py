import sys

n,m = map(int,sys.stdin.readline().split())
p = []
for i in range(m):
    p.append(int(sys.stdin.readline()))

price = 0
margin = 0
for i in p:
    temp = 0
    egg = n
    for j in range(m):
        if egg<=0:
            break
        if p[j]>=i:
            temp+=i
            egg -=1
    if temp>margin:
        margin = temp
        price = i

print(str(price)+" "+str(margin))
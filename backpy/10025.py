import sys

n,k = map(int,sys.stdin.readline().split())
jail = {}
for i in range(n):
    g,x = map(int,sys.stdin.readline().split())
    jail[x] = g

result = 0
roof = max(jail.keys())
tail = 0
head = 2*k
for i in range(k,roof+1):
    temp = 0
    for j in jail.keys():
        if j>=tail and j <= head:
            temp+=jail[j]
    result = max(temp,result)
    tail +=1
print(result)
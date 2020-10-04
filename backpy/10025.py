import sys

n,k = map(int,sys.stdin.readline().split())
jail = {}
for i in range(n):
    g,x = map(int,sys.stdin.readline().split())
    jail[g] = x

result = 0
roof = max(jail.keys())
tail = 0
head = 2*k
for i in range(head,roof+1):
    temp = 0
    for j in jail.keys():
        if j>=tail and j <= head:
            temp+=jail[j]
    result = max(temp,result)
    tail +=1
    head +=1

print(result)
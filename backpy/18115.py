import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a.reverse()
result = deque()

num = 1
for i in a:
    if i ==1:
        result.appendleft(num)
    elif i==2:
        result.insert(1,num)
    elif i==3:
        result.append(num)
    num+=1

for i in result:
    print(i,end=" ")

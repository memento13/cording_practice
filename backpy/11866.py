import sys
from collections import deque

N,K = map(int,sys.stdin.readline().split())
qu = deque()
for i in range(1,N+1):
    qu.append(i)

print("<",end="")
while (qu):
    for i in range(K-1):
        qu.append(qu.popleft())
    print(qu.popleft(),end="")
    if qu:
        print(", ",end = "")
print(">")
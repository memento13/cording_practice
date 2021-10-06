import sys

N = int(sys.stdin.readline())
date = [0]*367

for _ in range(N):
    S,E = map(int, sys.stdin.readline().split())
    for i in range(S,E+1):
        date[i] +=1

area = 0
high = 0
width = 0
for i in date:
    if i==0:
        area += width*high
        width = 0
        high = 0
    elif i>0 and width==0:
        width =1
        high = i
    elif i>0 and i>high:
        width +=1
        high = i
    else:
        width += 1

print(area)
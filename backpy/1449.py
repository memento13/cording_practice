import sys

N,L = map(int,sys.stdin.readline().split())

hole = list(map(int,sys.stdin.readline().split()))
hole.sort()

cover = 0
tapeUsed = 0
for i in range(N):
    if cover<hole[i]:
        tapeUsed+=1
        cover = hole[i]+L-1
print(tapeUsed)
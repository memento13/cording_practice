import sys
sys.setrecursionlimit(100000)
N = int(sys.stdin.readline())
house = []
result = 1000000
for _ in range(N):
    r,g,b = map(int,sys.stdin.readline().split())
    house.append([r,g,b])

for i in range(1,N):
    house[i][0] = min(house[i-1][1],house[i-1][2])+house[i][0]
    house[i][1] = min(house[i-1][0],house[i-1][2])+house[i][1]
    house[i][2] = min(house[i-1][0],house[i-1][1])+house[i][2]

print(min(house[N-1][0],house[N-1][1],house[N-1][2]))
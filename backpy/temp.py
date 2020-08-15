"""
def battle(i, j):
    stack = [(i, j)]
    visit[i][j] = True
    s = w = 0
    while stack:
        i, j = stack.pop()
        if grid[i][j] == 'v': w+= 1
        elif grid[i][j] == 'k': s+= 1
        for ni, nj in (i-1,j), (i+1,j), (i,j-1), (i,j+1):
            if grid[i][j] == "#" or visit[ni][nj]: continue
            visit[ni][nj] = True
            stack.append((ni,nj))
    if s > w: w = 0
    else: s = 0
    return s, w

n, m = map(int,input().split())
grid = [list(input()) for i in range(n)]
visit = [[False]*m for i in range(n)]
sheep = 0
wolf = 0
for i in range(n):
    for j in range(m):
        if visit[i][j]: continue
        if grid[i][j] == 'v' or grid[i][j] == 'k':
            s, w = battle(i, j)
            sheep+= s; wolf+= w
print(sheep, wolf)
"""
li = [True,True,True,True]
i = 0
while(li[0]==True or li[1]==True or li[2]==True or li[3]==True):
    li[i]=False
    i+=1
    print("%d 가능" %i)
print(li)
print("%d 불가능" %i)
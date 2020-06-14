N,M=map(int,input().split())

numList = []
for i in range(N):
    numList.append(int(i+1))
visited = []
for i in range(N):
    visited.append(False)

board = []

def dfs(depth):
    if depth==M:
        print(*board)
        return
    for i in range(N):
        if(visited[i]):
            continue
        visited[i]=True
        board.append(numList[i])
        dfs(depth+1)
        board.pop()
        for j in range(i+1,N):
            visited[j] = False
dfs(0)
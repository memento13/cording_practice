"""
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
"""
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
        visited[i]=False

dfs(0)
    
N,M=map(int,input().split())

numList = []
for i in range(N):
    numList.append(int(i+1))
visited = []
for i in range(N):
    visited.append(False)

board = []

def func(depth):
    if depth==M:
        print (*board)
        return
    for i in range(N):
        if(visited[i]):
            continue
       
        board.append(numList[i])
        func(depth+1)
        visited[i]=True
        board.pop()
        for j in range(N):
            visited[j] = False

func(0)
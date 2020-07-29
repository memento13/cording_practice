from sys import stdin as st

R,C = map(int,st.readline().split())
board = []
MAX = 1
visited = []
for i in range(R):
    board.append(list(st.readline().strip()))

def DFS(i,j,count):
    global MAX
    if count>MAX:
        MAX = count
    if board[i][j] not in visited:
        count+=1
        visited.append(board[i][j])
        if (0<=(i+1)<R) and (0<=(j)<C):
            DFS(i+1,j,count)
        if (0<=(i-1)<R) and (0<=(j)<C):
            DFS(i-1,j,count)
        if (0<=(i)<R) and (0<=(j+1)<C):
            DFS(i,j+1,count)
        if (0<=(i)<R) and (0<=(j-1)<C):
            DFS(i,j-1,count)
        visited.remove(board[i][j])
    else:
        return

DFS(0,0,0)
print(MAX)
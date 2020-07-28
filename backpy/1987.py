from sys import stdin as st

R,C = map(int,st.readline().split())
board = []
MAX = 0
visited = [0]*26
for i in range(R):
    board.append(list(st.readline().strip()))

def DFS(i,j,count):
    global MAX
    if i>R-1 or i<0:
        return
    if j>C-1 or j<0:
        return
    else:
        temp = ord(board[i][j])-ord("A")
        if visited[temp]==0:
            visited[temp] = 1
            count+=1
            if count>MAX:
                MAX = count
            DFS(i+1,j,count)
            DFS(i-1,j,count)
            DFS(i,j+1,count)
            DFS(i,j-1,count)
        else:
            return
            
DFS(0,0,0)
print(MAX)
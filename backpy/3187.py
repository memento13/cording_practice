
field = list()
visited=[]
global v
global k
v=0
k=0
R,C = map(int,input().split())
for i in range(R):
    field.append(list(input()))
    visited.append([False for i in range(C)])

def counter():
    global v
    global k
    if k>v:
        v=0
    else:
        k=0

def bfs(i,j):
    global v
    global k
    if i<0 or i>R-1:
        return
    if j<0 or j>C-1:
        return
    if visited[i][j] == True:
        return
    else:
        visited[i][j] = True
        if field[i][j] == '#':
            return
        else:
            if field[i][j]=='v':
                v=v+1
            elif field[i][j] =='k':
                k=k+1
            bfs(i+1,j)
            bfs(i-1,j)
            bfs(i,j-1)
            bfs(i,j+1)
total_v=0
total_k=0

for i in range(R):
    for j in range(C):
        v=0
        k=0
        bfs(i,j)
        counter()
        total_k=total_k+k
        total_v = total_v+v

print(total_k,total_v)

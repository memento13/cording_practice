import sys

N = int(sys.stdin.readline())
tree = []
for i in range(N):
    tree.append(list(map(int,sys.stdin.readline().split())))

for i in range(N-1):
    for j in range(len(tree[i+1])):
        if j ==0 :
            tree[i+1][j] = tree[i+1][j]+tree[i][j]
        elif j==len(tree[i+1])-1:
            tree[i+1][-1] = tree[i+1][-1]+tree[i][-1]
        else:
            tree[i+1][j] = tree[i+1][j]+max(tree[i][j-1],tree[i][j])
        
temp = []
for i in tree[N-1]:
    temp.append(i)
print(max(temp))
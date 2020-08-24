import sys

N = int(sys.stdin.readline())
tree = []
result = []
for i in range(N):
    tree.append(list(map(int,sys.stdin.readline().split())))

for i in range(N-1):
    temp = []
    for j in range(len(tree[i+1])):
        if j ==0 or j == len(tree[i+1])-1:
            temp.append(tree[i+1][j-1]+tree[i][j-1])
        else:
            temp.append(tree[i][j-1]+tree[i+1][j])
            temp.append(tree[i][j]+tree[i+1][j])
    result.append(temp)
        
temp = []
for i in result[N-1]:
    temp.append(i)
print(max(temp))
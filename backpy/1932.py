import sys

N = int(sys.stdin.readline())
tree = []
for i in range(N):
    tree.append(list(map(int,sys.stdin.readline().split())))

for i in range(N-1):
    for j in range(len(tree[i])):
        tree[i+1][j] = 
print(tree)
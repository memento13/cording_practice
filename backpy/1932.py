import sys

N = int(sys.stdin.readline())
tree = []
for i in range(N):
    tree.append(list(map(int,sys.stdin.readline().split())))

for i in range(N-1):
    for j in range(len(tree[i+1])):
        tree[i+1][j] += tree[i][j//2]
temp = []
for i in tree[N-1]:
    temp.append(i)
print(max(temp))
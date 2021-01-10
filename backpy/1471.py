import sys

n = int(sys.stdin.readline())
way = {}

for i in range(1,n+1):
    move = 0
    for j in str(i):
        move+=int(j)
    next = (i+move)%n
    if next==0:
        next = n
    way[i]  = next

result = 0
for i in range(1,n+1):
    visited = []
    now = i
    while True:
        if now in visited:
            result = max(len(visited),result)
            break
        else:
            visited.append(now)
            now = way[now]
    
print(result)

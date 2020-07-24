import sys

n = int(sys.stdin.readline())
rope = []
for i in range(n):
    rope.append(int(sys.stdin.readline()))
    
rope.sort(reverse=True)
maxWeight = 0
for i in range(n):
    temp = rope[i]*(i+1)
    if maxWeight<temp:
        maxWeight = temp

print(maxWeight)

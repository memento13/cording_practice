import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
length = [0]*n

for i in range(n):
    for j in range(i):
        if a[i]>a[j] and length[i]<length[j]:
            length[i] = length[j]
    length[i]+=1

print(max(length))
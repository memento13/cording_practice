import sys

N = int(sys.stdin.readline())
ilist = list(map(int,sys.stdin.readline().strip().split()))
num = list([0]*100001)
result = 0
for i in ilist:
    num[i]+=1

for j in range(100000,-1,-1):
    if num[j]==j:
        print(j)
        exit(0)
print(-1)
import sys

n = int(sys.stdin.readline())
result = []
for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    temp.append(i+1)
    result.append(temp)
result = sorted(result,key = lambda x : (-x[0],x[1],x[2]))
print(result[0][-1])
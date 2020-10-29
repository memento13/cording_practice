import sys

n = int(sys.stdin.readline())
x = list(map(int,sys.stdin.readline().split()))

result = 0
xlen = len(x)
for i in x:
    for j in x:
        result += abs(i-j)
print(result)

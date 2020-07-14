import sys

T = int(sys.stdin.readline())
result = []
for i in range(T):
    N,M = map(int,sys.stdin.readline().split())
    if N>11 and M>3:
        result.append(M*11+4)
    else:
        result.append(-1)
for i in range(T):
    print(result[i])

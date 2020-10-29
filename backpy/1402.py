import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a,b = map(int,sys.stdin.readline().split())
    print('yes')

# 6 1
# 3 2 1 -1 -1 -1 -1 -1 -1 1
#     6 -6 6 -6  6  -6  6 6 곱
#     6 5  4  3  2  1 0 1 b값
import sys

N = int(sys.stdin.readline())

first = list(map(int,sys.stdin.readline().split()))
second = list(map(int,sys.stdin.readline().split()))

first +=second
result = 0
for i in first:
    result+=abs(i)
print(result)
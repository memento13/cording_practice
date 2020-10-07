import sys

n = int(sys.stdin.readline())

result = 64
while n%2==0:
    result -=1
    n = n/2
print(result)
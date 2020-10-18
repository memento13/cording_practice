import sys

T = int(sys.stdin.readline())

for _ in range(T):
    a,b = map(int,sys.stdin.readline().split())
    result = a**2//b**2
    if a%b>0:
        result +=1
    print(result)
    
import sys

n = int(sys.stdin.readline())
temp =0
if n%2==1:
    temp = (n//2)+1

result = sum(map(int,sys.stdin.readline().split()))

a = ((n+1)*(n//2))+temp
result = result-a
print(result+n)

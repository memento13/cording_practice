import sys
a,b,c = (map(int,sys.stdin.readline().split()))
result1 = a*b/c
result2 = a/b*c
if result1>result2:
    print("%d"%result1)
else:
    print("%d"%result2)
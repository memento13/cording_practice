import sys

n,w,h,l = map(int,sys.stdin.readline().split())
result = (w//l)*(h//l)
if result>n:
    result = n
print(result)
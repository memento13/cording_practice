import sys

n = int(sys.stdin.readline())
count = 0
while(n>0):
    if n%5==0:
        print("%d" %(count+n/5))
        sys.exit(0)
    else:
        n-=2
        count+=1
if n==0:
    print(count)
else:
    print(-1)
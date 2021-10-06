import sys

N = int(sys.stdin.readline())
machines = list(map(int,sys.stdin.readline().split()))
sorted(machines)
a = []
b = []
c = 0

if N==1:
    c = machines[0]
else:
    if N%2==1:
        a = machines[:N//2]
        b = machines[N//2:N-1]
        b.reverse()
        c = machines[-1]
    else:
        a = machines[:N//2]
        b = machines[N//2:]
        b.reverse()
        c = a[0]+b[0]

    for i,j in zip(a,b):
        c = max(c,i+j)

print(c)
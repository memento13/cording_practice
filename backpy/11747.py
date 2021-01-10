import sys

n = int(sys.stdin.readline())
d = []
lines = n//19
if n%19>0:
    lines+=1
for _ in range(lines):
    d+=list(map(int,sys.stdin.readline().strip().split()))
numbers = set(d)
for i in range(n):
    now = str(d[i])
    for j in range(i+1,n):
        now = now+str(d[j])
        numbers.add(int(now))

result = 0
while True:
    if result in numbers:
        result+=1
    else:
        print(result)
        exit(0)
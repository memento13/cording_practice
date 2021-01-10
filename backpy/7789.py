import sys

a,b = map(str,sys.stdin.readline().strip().split(' '))
result = int(b+a)
a = int(a)
for i in range(2,a//2):
    if a%i==0:
        print('No')
        exit(0)
for i in range(2,result//2):
    if result%i==0:
        print('No')
        exit(0)
print('Yes')
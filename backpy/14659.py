import sys

N = int(sys.stdin.readline())
result = list(map(int,sys.stdin.readline().split()))
count = 0
priv = 0
Max = result[0]
for i in range(1,N):
    if Max>result[i]:
        count +=1
    else:
        Max = result[i]
        if count>priv:
            priv = count
        count = 0
if priv>count:
    print(priv)
else:
    print(count)
            


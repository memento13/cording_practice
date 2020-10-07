import sys

context  = str(sys.stdin.readline().strip())
space = int(sys.stdin.readline())
key = list(map(int, sys.stdin.readline().split()))

if context.count(' ')>space:
    print(-1)
    exit(0)
priv = '0'
for i in context:
    if priv == i:
        continue
    elif 'A' <= i <= 'Z':
        key[ord(i.lower())-97] -=1
        priv = i
    elif i==' ':
        space -=1
        priv = i
    else:
        key[ord(i)-97]-=1
        priv = i

result = ''
context = list(context.split())

for i in context:
    result = result + i[0].upper()
    
for i in result:
    if priv == i:
        continue
    elif 'A' <= i <= 'Z':
        key[ord(i.lower())-97] -=1
        priv = i
    elif i==' ':
        space -=1
        priv = i
    else:
        key[ord(i)-97]-=1
        priv = i

for i in key:
    if 0>i:
        print(-1)
        exit(0)


print(result)
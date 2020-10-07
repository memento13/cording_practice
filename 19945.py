import sys

cc = str(sys.stdin.readline().strip())

bit = []
if len(cc) >4:
    while len(cc)>4:
        bit.append(cc[0:4])
        cc = cc[4:]
bit.append(cc)
def func(b):
    result =''
    for i in range(len(b)):
        if b[i] == '1':
            result+=str(2**(len(b)-i))
    return result

ans=''
for i in bit:
    ans+=func(i)
print(ans)
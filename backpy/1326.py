import sys

n = int(sys.stdin.readline())
br = list(map(int,sys.stdin.readline().split()))
a,b = map(int,sys.stdin.readline().split())
a= a-1
b=b-1
flag = False
if a>b:
    flag = True
result = 10001

def func(now,jump,tried):
    global result
    if now+jump==b:
        tried+=1
        result = min(result,tried)
        return
    now += jump
    if now>b:
        return
    doll = br[now]
    for i in range(1,b-now):
        func(now,doll*i,tried+1)

def func2(now,jump,tried):
    global result
    if now-jump==a:
        tried+=1
        result = min(result,tried)
        return
    now -= jump
    if now<a:
        return
    doll = br[now]
    tried +=1
    for i in range(now-a):
        func2(now,doll*i,tried)

if flag:
    temp = a
    a=b
    b=temp
    br.reverse()
for i in range(b-a+1):
    doll = br[a]
    func(a,doll*i,0)
# if flag:
#     for i in range(a-b+1):
#         doll = br[b]
#         func2(b,doll*i,0)
# else:
#     for i in range(b-a+1):
#         doll = br[a]
#         func(a,doll*i,0)

if result ==10001:
    result = -1
print(result)

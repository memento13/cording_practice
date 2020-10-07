import sys

ans = list(sys.stdin.readline().split())
result =0
def func(score,stack,priv,now,num):
    global result
    if num == 9:
        if ans[num]==str(now):
            score+=1
        if num>=5:
            result +=1
        return
    if stack==2 and priv==now:
        return
    num+=1
    if ans[num]==str(now):
        score+=1
    if priv == now:
        stack+=1
    for i in range(1,6):
        func(score,stack,now,i,num)

for a in range(1,6):
    func(0,0,0,a,0)
print(result)
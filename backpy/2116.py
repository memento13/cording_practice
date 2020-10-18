import sys
sys.setrecursionlimit(100000)
t = int(sys.stdin.readline())
dice = []
for _ in range(t):
    temp = list(map(int,sys.stdin.readline().split()))
    dice.append(temp)

dic = {0:5,1:3,2:4,5:0,3:1,4:2}
# a:f, b:d, c:e
# 0:5, 1:3, 2:4
result = 0
def tower(now,value,priv):
    global result
    if now == t:
        result = max(value,result)
        return
    tempdice = dice[now].copy()
    nextpriv = tempdice[dic[tempdice.index(priv)]]
    tempdice.remove(nextpriv)
    tempdice.remove(priv)
    value += max(tempdice)
    tower(now+1,value,nextpriv)

for i in range(6):
    first = dice[0][i]
    tempdice = dice[0].copy()
    firstindex = dic[tempdice.index(first)]
    priv = tempdice[firstindex]
    tempdice.remove(priv)
    tempdice.remove(first)
    value = max(tempdice)
    tower(1,value,priv)

print(result)

import sys

N = int(sys.stdin.readline())
house = []
result = 1000000
for _ in range(N):
    r,g,b = map(int,sys.stdin.readline().split())
    house.append([r,g,b])

def func(i,priv,total):
    global result
    if i==N:
        result = min(result,total)
        return
    temp = list(house[i])
    temp.pop(priv)
    total+=min(temp)
    func(i+1,house[i].index(min(temp)),total)

for i in range(3):
    func(1,i,house[0][i])
print(result)
import sys

N = int(sys.stdin.readline())
ingredient = []
for _ in range(N):
    sour,bitter = map(int,sys.stdin.readline().split())
    ingredient.append([sour,bitter])
flavor = []

def func(s,b,i):
    global flavor
    if i==N:
        return
    flavor.append(abs((s*ingredient[i][0])-(b+ingredient[i][1])))
    func(s,b,i+1)
    func((s*ingredient[i][0]),(b+ingredient[i][1]),i+1)

func(1,0,0)
print(min(flavor))
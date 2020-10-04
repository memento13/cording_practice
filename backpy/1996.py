import sys

N = int(sys.stdin.readline())
map = []
for i in range(N):
    map.append(list(sys.stdin.readline().strip()))

result = []
for i in range(N):
    temp = []
    for j in range(N):
        if map[i][j]=='.':
            temp.append(0)
        else:
            temp.append('*')
            map[i][j] = int(map[i][j])
    result.append(temp)

compassi = [-1,-1,-1,0,0,1,1,1]
compassj = [-1,0,1,-1,1,-1,0,1]


for i in range(N):
    for j in range(N):
        if result[i][j]=='*':
            for a in range(8):
                if i+compassi[a]<0 or i+compassi[a]>N-1 or j+compassj[a]<0 or j+compassj[a]>N-1:
                    continue
                if result[i+compassi[a]][j+compassj[a]] != '*':
                    result[i+compassi[a]][j+compassj[a]] += map[i][j]
                

for i in range(N):
    for j in range(N):
        if result[i][j] =='*':
            continue
        if result[i][j] >=10:
            result[i][j] = 'M'
        result[i][j] = str(result[i][j])

for i in result:
    print(''.join(i))

import sys

img_i = []
y,x = map(int,sys.stdin.readline().split())
for _ in range(y):
    temp = list(map(int,sys.stdin.readline().split()))
    img_i.append(temp)
t = int(sys.stdin.readline())
jx = x-2
jy = y-2
result = 0

for i in range(jy):
    for j in range(jx):
        temp = []
        for fy in range(i,i+3):
            for fx in range(j,j+3):
                temp.append(img_i[fy][fx])
        temp.sort()
        if temp[4] >=t:
            result+=1

print(result)
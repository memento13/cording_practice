import sys

n = int(sys.stdin.readline())
result = 0
temp = 0
for i in range(n):
    d,v = map(int,sys.stdin.readline().split())
    temp = d+temp
    if i==0:
        result+=v
        continue

    if v-temp<0:
        rest = v-temp
        temp = d+abs(rest)
        continue
    result+=v-temp
    temp = d
    
print(result)
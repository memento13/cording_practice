import sys
# n까지의 약수의 갯수 합으로 가능
n = int(sys.stdin.readline())
result = 0
s = set()
same = set()
for i in range(1,n+1):
    for j in range(1,n+1):
        if i*j<=n:
            if i==j:
                same.add(i)
                continue
            s.add((i,j))
            s.add((j,i))
        else:
            break
result = (len(s)//2)+len(same)
print(result)
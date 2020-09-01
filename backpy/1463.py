import sys
"""
X = int(sys.stdin.readline())
result = [0 for _ in range(X+1)]
index = 0
while(index<X+1):
    if index<2:
        result[index]=0
    else:
        count = X
        if index%3==0:
            count = min(count,result[index//3])
        if index%2==0:
            count = min(count,result[index//2])
        count = min(count,result[index-1])
        result[index] = count+1
    index+=1
print(result[X])
"""
# bestcode

save = {1:0, 2:1}
def frog(n):
    if n in save:
        return save[n]
    m = 1+min(frog(n//2)+n%2, frog(n//3)+n%3)
    save[n] = m
    return m

n = int(input())
print(frog(n))

import sys

n = int(sys.stdin.readline())
if n <=10: #10이하의 숫자
    print(n)
    exit(0)

result = 10
now = 11
while now<=n:
    temp = now
    total = 0
    temp = list(map(int,str(temp)))
    total = sum(temp)
    # while temp>0:
    #     total += temp%10
    #     temp = temp//10
    if now%total==0:
        result+=1
    now+=1
print(result)


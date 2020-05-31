
def func(n):
    result = n
    while n>0:
        result += n%10
        n = n//10
    return result

N = int(input())
result=0
for i in range(1,N+1):
    temp= func(i)
    
    if temp==N:
        result=i
        break

if result==0:
    print(0)
else:
    print(result)
    
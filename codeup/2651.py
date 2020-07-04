n,k = map(int,input().split())
count = 0
def func(N,K):
    global count
    if N==n and k==K:
        count += 1
        return
    elif N>n or K>k:
        return
    else:
        func(N+1,K)#자리에 앉지 않는 경우
        func(N+1,K+1) #자리에 앉는 경우
        
func(0,0)
print(count)
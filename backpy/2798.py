N,M=map(int,input().split())
cards=[]

cards = list(map(int, input().split(' ')))
result = 0
result_abs= M-result
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            tmpresult=cards[i]+cards[j]+cards[k]
            tmpresult_abs = abs(M-tmpresult)

            if(tmpresult<=M and tmpresult_abs<result_abs):
                result=tmpresult
                result_abs=tmpresult_abs

print(result)
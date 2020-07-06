N = int(input())
O = int(input())
result = O//(N-1)

if(O%(N-1)>0):
    print(result*N,result*N+1)
    
elif(O%(N-1)==0):
    print(O+result-1,O+result)
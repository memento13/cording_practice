import sys
N,M=map(int,input().split())
List=list(reversed(sorted(map(int,sys.stdin.readline().split()))))
ansub=set()
for i in range(N-2):
   for j in range(i+1,N-1):
      for k in range(j+1,N):
         if List[i]+List[j]+List[k]==M:
            print(M)
            sys.exit()
         else:
            if List[i]+List[j]+List[k]<M:
               ansub.add(List[i]+List[j]+List[k])
               break
print(max(ansub))
         

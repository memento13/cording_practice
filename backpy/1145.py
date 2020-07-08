A,B,C,D,E = map(int,input().split())
result = 1
while True:
    count = 0
    if(result%A==0):
        count= count+1
    if(result%B==0):
        count= count+1
    if(result%C==0):
        count= count+1
    if(result%D==0):
        count= count+1
    if(result%E==0):
        count= count+1
    if count>=3:
        break
    result = result+1

print(result)
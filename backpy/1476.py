import sys

E,S,M = map(int,sys.stdin.readline().split())
result = 1
while True:
    if result %15==E or (E==15 and result %15 ==0):
        if result %28==S or (S==28 and result %28 ==0):
            if result %19==M or (M==19 and result %19==0):
                break
    result +=1

print(result)
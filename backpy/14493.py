import sys

N = int(sys.stdin.readline())

now = 0
for _ in range(N):
    a,b = map(int,sys.stdin.readline().split()) 
    #a는 간격 나타남, b는 침입자 탐지시간
    save = now %(a+b)
    if save <b: #이동불가인 경우
        now+=b-save 
    now+=1 #이동시 1시간 플러스

print(now)

import sys

N,T,P = map(int,sys.stdin.readline().split())
member = [] #점수,문제 맞은 횟수,이름
test = [0]*T #문제 틀린사람 수 저장배열
arr = list() #입력값 복사

for i in range(N):
    member.append([0,0,i])

for i in range(N):
    case = list(map(int,sys.stdin.readline().split())) #입력값
    arr.append(case) #입력값 저장
    for j in range(T): #입력값 분석
        if case[j] ==0: #문제 틀린경우
            test[j] +=1 #문제번호 배열에 틀린사람수 증가
    
for i in range(N):
    score = 0 #개개인 점수 초기화
    mt = 0 #문제 맞은 갯수 초기화
    for j in range(T):
        if arr[i][j] ==1: #문제 맞은 경우
            score+=test[j] #점수 계산
            mt+=1 #문제 맞은 갯수 계산
    member[i][0] = score # 해당 멤버 배열의 점수 입력
    member[i][1] = mt #해당 멤버 배열의 맞은 문제수 입력

#점수에 따라 sort 만약 같은 점수인 경우 문제 맞은 갯수에 따라 sort =  -x[0],-x[1]
#앞의 두 조건이 같은경우 이름의 순서에 맞춰서 sort = x[2]
member = sorted(member,key = lambda x: (-x[0],-x[1],x[2]))

for i in range(N):
    if member[i][2] == P-1:
        print(member[i][0],i+1) #순위는 1부터 시작하기 때문
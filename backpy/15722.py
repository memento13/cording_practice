"""
변의 길이
변길이 내에서의 시도횟수 (max 2)
홀수일때 위 오른쪽
짝수일때 아래 왼쪽
위 = y+1    아래 = y-1
왼쪽 = x-1  오른쪽 x+1
시간단위로 구별
변의길이 = side
시도횟수 = case
시간 = time
시작시 1 0 0 0

"""
N = int(input())
def func(side,case,time,x,y):
    if time == N:
        print(x,y)
        return
    else:
        time = time+1
        case = case+1
        if side%2==1: #변의 길이 홀수일때
            if case <=side:
                func(side,case,time,x,y+1)
            else:
                if case>=side*2:
                    case = 0
                func(side+1,case,time,x+1,y)
        else:
            if case <=side:
                func(side,case,time,x,y-1)
            else:
                if case>=side*2:
                    case = 0
                func(side+1,case,time,x-1,y)

func(1,0,0,0,0)
    


import sys

def func():
    r,c = map(int,sys.stdin.readline().split()) #행렬
    board = [[0 for col in range(c+2)]for row in range(r+2)]#가장자리가 0인 보드 생성
    #행렬입력
    for row in range(1,r+1):
        temp = list(map(int,sys.stdin.readline().strip()))
        for col,i in enumerate(temp,1):
            board[row][col] = i
    
    dis = [[-1,0],[0,-1],[0,1],[1,0]] #위,왼쪽,오른쪽,아래 방향지시
    result = 0

    for row in range(1,r+1):
        for col in range(1,c+1):
            now = board[row][col] #현재 위치의 값
            if now>0: 
                result+=2 #아랫면 윗면 넓이
                for d in dis: #4방향을 비교하면서 겉넓이 구하기
                    compare = board[row-d[0]][col-d[1]]
                    if now > compare:
                        result+=(now-compare)
    print(result)



def run():
    t = int(sys.stdin.readline())
    for _ in range(t):
        func()

if __name__=='__main__':
    run()

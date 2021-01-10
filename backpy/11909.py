import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
board = []
result = 999999
for _ in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    board.append(temp)

def move(prevx,prevy,x,y,money,n):
    global result
    # 최대값보다 넘어갈때
    if money>=result:
        return
    # 배열 아웃오브레인지
    if x>n-1 or y>n-1:
        return
    # 끝에 도달한 경우
    if x==n-1 and y==n-1:
        if board[prevy][prevx]<=board[y][x]:
            if board[prevy][prevx]-board[y][x]==0:
                money+=1
            else:
                money+=(board[y][x]-board[prevy][prevx])+1
        result = min(money,result)
        return
    # 처음 시작
    if x==0 and y==0:
        move(x,y,x+1,y,money,n)
        move(x,y,x,y+1,money,n)
    # 중간
    else:
        if board[prevy][prevx]<=board[y][x]:
            if board[y][x]-board[prevy][prevx]==0:
                move(x,y,x,y+1,money+1,n)
                move(x,y,x+1,y,money+1,n)
            else:
                move(x,y,x,y+1,money+(board[y][x]-board[prevy][prevx])+1,n)
                move(x,y,x+1,y,money+(board[y][x]-board[prevy][prevx])+1,n)
        else:
            move(x,y,x,y+1,money,n)
            move(x,y,x+1,y,money,n)
        

move(0,0,0,0,0,n)
print(result)
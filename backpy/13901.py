import sys
sys.setrecursionlimit(100000)
R,C = map(int,sys.stdin.readline().split())
board = [[False]*C for _ in range(R)]
k=int(sys.stdin.readline())
for _ in range(k):
    br,bc = map(int,sys.stdin.readline().split())
    board[br][bc] = True
sr,sc = map(int,sys.stdin.readline().split())
qu = list(map(int,sys.stdin.readline().split()))
dirR = [0,-1,1,0,0]
dirC = [0,0,0,-1,1]
quImpossible = 0

def Move(r,c,q):
    global quImpossible
    if quImpossible == 4:
        print(r,c)
        return
    tempR = r+dirR[qu[q]]
    tempC = c+dirC[qu[q]]
    if(tempR<0 or tempR>=R or tempC<0 or tempC>=C or board[tempR][tempC]==True):
        quImpossible+=1
        Move(r,c,(q+1)%4)
        return
    board[r][c] = True
    quImpossible = 0
    Move(tempR,tempC,q)
    return

Move(sr,sc,0)



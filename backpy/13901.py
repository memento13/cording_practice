import sys

R,C = map(int,sys.stdin.readline().split())
board = [[0]*C]*R
k=int(sys.stdin.readline())
for _ in range(k):
    br,bc = map(int,sys.stdin.readline().split())
    board[br][bc] = 1
sr,sc = map(int,sys.stdin.readline().split())
qu=list(map(int,sys.stdin.readline().strip().split()))
qupossible = [True]*4
q=0
def move(r,c):
    global q
    global qupossible
    if r>=R or r<0 or c>=C or c<0 or board[r][c]>0:
        qupossible[q%4] = False
        q+=1
        return
    else:
        qupossible = [True]*4
        while(qupossible[0]==True or qupossible[1]==True or qupossible[2]==True or qupossible[3]==True):
            if qu[q%4]==1:
                move(r-1,c)
            elif qu[q%4]==2:
                move(r+1,c)
            elif qu[q%4] ==3:
                move(r,c-1)
            elif qu[q%4] ==4:
                move(r,c+1)
        return r,c
resultr,resultc = move(sr,sc)
print(resultr,resultc)


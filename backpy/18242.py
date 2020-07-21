import sys

N,M = map(int,sys.stdin.readline().split())
board = []
for i in range(N):
    board.append(list(sys.stdin.readline().strip()))

def findStart():
    for i in range(N):
        for j in range(M):
            if board[i][j]=="#":
                return i,j

def findEnd():
    for i in reversed(range(N)):
        for j in reversed(range(M)):
            if board[i][j]=="#":
                return i,j

def colCK(x1,x2,y1):
    for i in range(x1,x2-1):
        temp = board[y1][i]+board[y1][i+1]+board[y1][i+2]
        temp = "".join(temp)
        if temp == "#.#":
            return True
    return False

def rowCK(y1,y2,x1):
    for i in range(y1,y2-1):
        temp = board[i][x1]+board[i+1][x1]+board[i+2][x1]
        temp = "".join(temp)
        if temp == "#.#":
            return True
    return False

Y1,X1 = findStart()
Y2,X2 = findEnd()

if colCK(X1,X2,Y1):
    print("UP")
elif colCK(X1,X2,Y2):
    print("DOWN")
elif rowCK(Y1,Y2,X1):
    print("LEFT")
elif rowCK(Y1,Y2,X2):
    print("RIGHT")

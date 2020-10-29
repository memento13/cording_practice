import sys

board = []
for _ in range(10):
    temp = list(sys.stdin.readline().strip())
    board.append(temp)

# 012
# 3 4
# 567
disx = [-1,0,1,-1,1,-1,0,1]
disy = [-1,-1,-1,0,0,1,-1,1]

def ComboCK(distance,x,y):
    combo = 0
    life = 1
    tempx = x
    tempy = y
    for i in range(5):
        tempx+=disx[distance]
        tempy+=disy[distance]
        if board[tempy][tempx] == '.'and life>0:
            combo+=1
            life-=1
        elif board[tempy][tempx] == 'X':
            combo+=1
        elif board[tempy][tempx] == 'O':
            break
    if combo==5:
        print(1)
        exit(0)
    return
for y in range(10):
    for x in range(10):
        if board[y][x] == 'X':
            if x<6:
                ComboCK(4,x,y)
                if y<6:
                    ComboCK(7,x,y)
                else:
                    ComboCK(6,x,y)
            if y<6:
                ComboCK(6,x,y)
print(0)
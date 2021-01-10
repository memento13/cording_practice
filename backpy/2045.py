import sys

board = []
for _ in range(3):
    temp = list(map(int,sys.stdin.readline().split()))
    board.append(temp)

avg = 0
flag = False
for a in range(3):
    if not 0 in board[a]:
        avg=sum(board[a])
        flag = True
        break

if flag==False:
    for y in range(3):
        temp = []
        for x in range(3):
            temp.append(board[y][x])
        if not 0 in temp:
            avg = sum(temp)
            flag = True
            break


            
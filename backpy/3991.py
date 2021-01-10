import sys

h,w,c = map(int,sys.stdin.readline().split())
color = list(map(int,sys.stdin.readline().split()))

board = [[0]*w for i in range(h)]
flag = True
h_now = h-1
w_now = 0
for i in range(c):
    left = color[i]
    for _ in range(left):
        if flag:
            board[h_now][w_now] = str(i+1)
            w_now+=1
            if w_now==w:
                flag = False
                h_now -=1
                w_now = w-1
        else:
            board[h_now][w_now] = str(i+1)
            w_now-=1
            if w_now==-1:
                flag = True
                h_now -=1
                w_now = 0

for i in board:
    print(''.join(i))

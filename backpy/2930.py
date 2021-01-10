import sys

r = int(sys.stdin.readline())
board = []
my = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())
for _ in range(n):
    board.append(list(sys.stdin.readline().strip()))

def func(a,b):
    if a==b:
        return 1
    if a=='S' and b=='P':
        return 2
    if a=='S' and b=='R':
        return 0
    if a=='P' and b=='S':
        return 0
    if a=='P' and b=='R':
        return 2
    if a=='R' and b=='P':
        return 0
    if a=='R' and b=='S':
        return 2
    
example = ['S','P','R']
dic = {'S':0,'P':0,'R':0}
win_result = 0
max_result = 0
for i in range(r):
    sang = my[i]
    dic = {'S':0,'P':0,'R':0}
    bround = []
    for j in range(n):
        temp = board[j][i]
        bround.append(temp)
        dic[temp]+=1
        win_result+=func(sang,temp)
    round_result = 0
    for j in example:
        temp = 0
        for k in bround:
            temp+=func(j,k)
        round_result = max(temp,round_result)
    max_result+=round_result

print(win_result)
print(max_result)



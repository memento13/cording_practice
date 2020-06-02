def w_cheaker(lst,i,j):
    count = 0
    for x in range(8):
        for y in range(8):
            if (x+y)%2==0:
                if lst[i+x][j+y]!='W':
                    count+=1
            else:
                if lst[i+x][j+y]!='B':
                    count+=1
    
    return count

def b_cheaker(lst,i,j):
    count = 0
    for x in range(8):
        for y in range(8):
            if (x+y)%2==0:
                if lst[i+x][j+y]!='B':
                    count+=1
            else:
                if lst[i+x][j+y]!='W':
                    count+=1
    
    return count


N,M=map(int,input().split())
board = [list(input()) for _ in range(N)]

result = 1048576

for i in range(N-7):
    for j in range(M-7):
        wmin=w_cheaker(board,i,j)
        bmin=b_cheaker(board,i,j)

        result = min(result,wmin,bmin)

print(result)

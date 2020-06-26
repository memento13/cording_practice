N = int(input())
count = 0
col = [False]*N
leftDia = [False]*(2*N-1)
rightDia = [False]*(2*N-1)

def QueenCK(row):
    global count
    if row == N:
        count += 1
        return
    for i in range(N):
        if not(col[i] or rightDia[row+i] or leftDia[row-i+N-1]):
            col[i] = rightDia[row+i]=leftDia[row-i+N-1] = True
            QueenCK(row+1)
            col[i] = rightDia[row+i]=leftDia[row-i+N-1] = False

QueenCK(0)
print(count)
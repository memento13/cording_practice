import sys

r,c = map(int,sys.stdin.readline().split())
parkinglot = []
parkpossible=[0,0,0,0,0]
for i in range(r):
    parkinglot.append(list(sys.stdin.readline().strip()))

def structCK(i,j):
    if i>r-2 or j >c-2 or parkinglot[i][j]=="#" or parkinglot[i][j+1]=="#" or parkinglot[i+1][j]=="#" or parkinglot[i+1][j+1]=="#":
        return False
    else:
        return True

def parktest(i,j):
    crashcar = 0
    for a in range(i,i+2):
        for b in range(j,j+2):
            if parkinglot[a][b] == "X":
                crashcar+=1
        
    return crashcar
        


for i in range(r):
    for j in range(c):
        if structCK(i,j):
            parkpossible[parktest(i,j)]+=1
        
for i in range(5):
    print(parkpossible[i])
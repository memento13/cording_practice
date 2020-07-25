import sys
import math

def score(x,y):
    x = abs(x)
    y = abs(y)
    dis = math.sqrt(float(x**2+y**2))
    if dis<=3:
        return 100
    elif dis<=6:
        return 80
    elif dis<=9:
        return 60
    elif dis<=12:
        return 40
    elif dis<=15:
        return 20
    else:
        return 0

result = []

def testInput():
    jp = list(map(float,sys.stdin.readline().split()))
    p1Score = score(jp[0],jp[1])+score(jp[2],jp[3])+score(jp[4],jp[5])
    p2Score = score(jp[6],jp[7])+score(jp[8],jp[9])+score(jp[10],jp[11])
    result.append([p1Score,p2Score])

def PrintResult():
    for p1,p2 in result:
        if p1>p2:
            temp = "PLAYER 1 WINS"
        elif p2>p1:
            temp = "PLAYER 2 WINS"
        else:
            temp = "TIE"
        print("SCORE: %d to %d, %s." %(p1,p2,temp))

N = int(sys.stdin.readline())
for i in range(N):
    testInput()

PrintResult()
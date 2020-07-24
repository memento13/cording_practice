import sys

N = int(sys.stdin.readline())
timeTable = []
count = 0
conftime = 0

for i in range(N):
    temp = list(map(int,sys.stdin.readline().split()))
    timeTable.append(temp)

timeTable = sorted(timeTable, key = lambda x : (x[1],x[0]))

for i in range(N):
    if conftime<=timeTable[i][0]:
        conftime = timeTable[i][1]
        count +=1
    
print(count)

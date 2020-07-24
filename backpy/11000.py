import sys

N = int(sys.stdin.readline())
timeTable = []
claTimeTable = [0]


for i in range(N):
    temp = list(map(int,sys.stdin.readline().split()))
    timeTable.append(temp)

timeTable = sorted(timeTable, key = lambda x : (x[1],x[0]))

for i in range(N):
    temp = len(claTimeTable)
    for j in range(temp): 
        if claTimeTable[j]<=timeTable[i][0]:
            claTimeTable[j] = timeTable[i][1]
            break
        else:
            claTimeTable.append(timeTable[i][1])
            break

print(len(claTimeTable))

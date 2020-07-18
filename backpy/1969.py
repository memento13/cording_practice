import sys

N,M = map(int,sys.stdin.readline().split())
DNA_list = []
for i in range(N):
    DNA_list.append(sys.stdin.readline().strip())

resultDNA=""
resultCount = 0

for i in range(M):
    alpa = [0,0,0,0]
    for j in range(N):
        if DNA_list[j][i] == 'A':
            alpa[0] +=1
        elif DNA_list[j][i] =='C':
            alpa[1] +=1
        elif DNA_list[j][i] =='G':
            alpa[2] +=1
        elif DNA_list[j][i] =='T':
            alpa[3] +=1
    alpaMAX = max(alpa)
    alpaIDX = alpa.index(alpaMAX)
    if alpaIDX == 0:
        resultDNA+='A'
    elif alpaIDX ==1:
        resultDNA += 'C'
    elif alpaIDX ==2:
        resultDNA += 'G'
    elif alpaIDX == 3:
        resultDNA +='T'
    resultCount += N-alpaMAX


print(resultDNA)
print(resultCount)

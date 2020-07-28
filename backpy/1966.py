import sys
from collections import deque

testcase = int(sys.stdin.readline())
printTestcase=[]

def func(doc,M):
    rank = 1
    while(len(doc)>0):
        temp = doc.popleft()
        def CompareStatus(t):
            for i in doc:
                if i[1]>t:
                    return False
            return True

        if CompareStatus(temp[1]):
            if M == temp[0]:
                printTestcase.append(rank)
                break
            rank+=1
        else:
            doc.append(temp)
        

def inputNM():
    N,M = map(int,sys.stdin.readline().split())
    status = list(map(int,sys.stdin.readline().split()))
    doc = deque()
    for i in range(N):
        doc.append((i,status[i]))
    func(doc,M)

for i in range(testcase):
    inputNM()

for i in printTestcase:
    print(i)
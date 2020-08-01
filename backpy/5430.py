from sys import stdin as st
from collections import deque

qu = deque()
testcase = int(st.readline())

def func(functionList,numlist):
    Rnum = 0
    while functionList:
        temp = functionList.popleft()
        if temp =='R':
            Rnum+=1
        elif temp == 'D':
            if not numlist:
                return "error"
            if Rnum%2==1:
                numlist.pop()
            else:
                numlist.popleft()
    if Rnum %2==1:
        numlist.reverse()
    return list(numlist)

for i in range(testcase):
    functionList = deque(st.readline().strip())
    trash = int(st.readline())
    if trash ==0:
        numlist = []
    else:
        numlist = list(map(int,st.readline().strip()[1:-1].split(',')))
        numlist = deque(numlist)
    
    print(func(functionList,numlist))

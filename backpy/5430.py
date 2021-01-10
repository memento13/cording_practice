from sys import stdin as st
from collections import deque

qu = deque()
testcase = int(st.readline())

def func(functionList,numlist):
    flag = True
    for i in functionList:
        if i == 'R':
            if flag:
                flag = False
            else:
                flag = True
        elif i=='D':
            if not numlist:
                return 'error'
            if flag:
                numlist.popleft()
            else:
                numlist.pop()
    
    if flag==False:
        numlist.reverse()
    return list(numlist)

for i in range(testcase):
    functionList = deque(st.readline().strip())
    trash = int(st.readline())

    
    if trash ==0:
        numlist = []
        tmp = st.readline()
    else:
        numlist = list(map(int,st.readline().strip()[1:-1].split(',')))
        numlist = deque(numlist)
    
    result = func(functionList,numlist)
    result = str(result).replace(' ','')
    print(result)

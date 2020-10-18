import sys
from collections import deque
sys.setrecursionlimit(100000)
result = 0


def greedy_func(now,total,leftLimit,rightLimit,inputList,Llist,Rlist):
    global result
    if now <leftLimit:
        for _ in range(len(inputList)):
            temp = inputList.popleft()
            Llist.append(temp)
            greedy_func(now+1,total,leftLimit,rightLimit,inputList,Llist,Rlist)
            inputList.append(Llist.pop())
    elif now<total:
        if Llist[0] == '0':
            return
        for _ in range(len(inputList)):
            temp = inputList.popleft()
            Rlist.append(temp)
            greedy_func(now+1,total,leftLimit,rightLimit,inputList,Llist,Rlist)
            inputList.append(Rlist.pop())
    else:
        if Rlist[0] == '0':
            return
        leftNum = ''.join(Llist)
        leftNum = int(leftNum)
        rightNum = ''.join(Rlist)
        rightNum = int(rightNum)
        result = min(result,(leftNum+rightNum))
    return

def func(string):
    global result
    # a = list(map(int,string.split()))
    inputList = deque(map(str,string[1:].split()))
    result = ''.join(inputList)
    result = int(result)
    total = int(string[0])

    greedy_func(0,total,total//2,total-(total//2),inputList,[],[])

def func(string):
    global result
    left = []
    right = []
    # a = list(map(int,string.split()))
    inputList = list(map(str,string[1:].split()))
    inputList.sort()
    count = inputList.count('0')

    temp = count
    while temp>0:
        inputList.remove('0')
    print(inputList)
    flag = True
    # for i in inputList:
    #     if flag:

    result = ''.join(inputList)
    result = int(result)

while True:
    string = sys.stdin.readline().strip()
    if string =='0':
        exit(0)
    func(string)
    print(result)
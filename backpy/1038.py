import sys
from collections import deque
def Decrease(priv,value):
    if value<10:
        if priv>value:
            return True
        else:
            return False
    temp = deque(str(value))
    nextpriv = int(temp.popleft())
    if nextpriv<priv:
        temp = ''.join(temp)
        Decrease(nextpriv,int(temp))
    else:
        return False

result = 0
case = -1
n = int(sys.stdin.readline())
while True:
    if case<10:
        result+=1
        case+=1
        if case == n:
            print(result)
            exit(0)
        continue
    temp = deque(str(result))
    priv = int(temp.popleft())
    temp = ''.join(temp)
    if Decrease(priv,int(temp)):
        case+=1
        if case == n:
            print(result)
            exit(0)
    result+=1

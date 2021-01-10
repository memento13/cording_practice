import sys
from collections import deque

def func():
    commend = deque(sys.stdin.readline().strip().split())
    for i in commend:
        if i=='L':
            if left_que:
                right_que.appendleft(left_que.pop())
            else:
                continue
        elif i=='D':
            if right_que:
                left_que.append(right_que.popleft())
            else:
                continue
        elif i =="B":
            if left_que:
                left_que.pop()
            else:
                continue
        elif i =="P":
            left_que.append(commend[1])
        else:
            continue
    

right_que = deque()
left_que = deque(list(sys.stdin.readline().strip()))
m = int(sys.stdin.readline())
for _ in range(m):
    func()
print(''.join(left_que),end='')
print(''.join(right_que))


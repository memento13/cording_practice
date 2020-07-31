import sys
from collections import deque

N = int(sys.stdin.readline())
qu = deque()

for i in range(N):
    cmd = list(sys.stdin.readline().split())

    if cmd[0] == "push_front":
        qu.insert(0,cmd[1])
    elif cmd[0] == "push_back":
        qu.append(cmd[1])
    elif cmd[0] == "pop_front":
        if not qu:
            print(-1)
        else:
            print(qu.popleft())
    elif cmd[0] == "pop_back":
        if not qu:
            print(-1)
        else:
            print(qu.pop())
    elif cmd[0] == "size":
        print(len(qu))

    elif cmd[0] == "empty":
        if not qu:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front": 
        if not qu:
            print(-1)
        else:
            print(qu[0])
    elif cmd[0] == "back":
        if not qu:
            print(-1)
        else:
            print(qu[-1])
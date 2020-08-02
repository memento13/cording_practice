import sys
from collections import deque

N = int(sys.stdin.readline())
qu = deque()

for i in range(N):
    cmd = list(sys.stdin.readline().split())

    if cmd[0] == "push":
        qu.append(cmd[1])
    elif cmd[0] == "pop":
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
    elif cmd[0] == "top":
        if not qu:
            print(-1)
        else:
            print(qu[-1])
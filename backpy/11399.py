import sys

N = int(sys.stdin.readline())
time = list(map(int,sys.stdin.readline().split()))

if N == 1:
    print(time[0])
else:
    time.sort()
    result = 0
    waitTime = 0

    for i in range(N):
        result += waitTime+time[i]
        waitTime += time[i]
    print(result)
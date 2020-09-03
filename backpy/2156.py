import sys

N = int(sys.stdin.readline())
step = []
for _ in range(N):
    step.append(int(sys.stdin.readline()))

result = [0 for _ in range(N)]
if N<3:
    print(sum(step))
else:
    result[0]=step[0]
    result[1]=step[0]+step[1]
    result[2] = max(step[1]+step[2],step[0]+step[2],result[1])

    for i in range(3,N):
        result[i] = (max(result[i-1],result[i-3]+step[i-1]+step[i],result[i-2]+step[i]))
    print(result[-1])
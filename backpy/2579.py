import sys

N = int(sys.stdin.readline())
step = []
for _ in range(N):
    step.append(int(sys.stdin.readline()))

step.reverse()
streak = 0
i=0
while(i<N-1):
    if streak<2:
        if i==N-2:
            step[i+1]+=step[i]
            i+=1
        else:
            if step[i+1]>step[i+2]:
                step[i+1]+=step[i]
                streak+=1
                i+=1
            else:
                step[i+2]+=step[i]
                streak=0
                i+=2
    else:
        streak=0
        step[i+1]+=step[i]
        i+=1
print(step[-1])
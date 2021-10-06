import sys

n = int(sys.stdin.readline())
rout = list(str(sys.stdin.readline().strip()))
cnt = 0

def func(start):
    try:
        if start == n-1:
            global cnt
            cnt = cnt+1
            return
        if start>=n:
            return
        if rout[start]=='1':
            func(start+1)
            func(start+2)
        else:
            return
    except:
        return
    

func(0)

print(cnt)
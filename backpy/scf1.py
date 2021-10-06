import sys


def timesplite(t):
    start = t[0:5]
    end = t[8:13]
    stime = (int(start[:2])*60)+(int(start[3:]))
    etime = (int(end[:2])*60)+(int(end[3:]))

    return stime,etime

n = int(sys.stdin.readline())

startTime, endTime = timesplite(sys.stdin.readline())
arr = []
for i in range(0,n-1):
    arr.append(sys.stdin.readline())
for i in arr:
    start, end = timesplite(i)
    if startTime<=start and start<endTime:
        startTime = start
    else:
        if start>endTime:
            print(-1)
            exit(0)
    if endTime>=end and end>startTime:
        endTime = end
    else:
        if end<startTime:
            print(-1)
            exit(0)

sh = startTime//60
sm = startTime%60
if sh<10:
    sh = '0'+str(sh)
if sm<10:
    sm = '0'+str(sm)
start  = str(sh)+':'+str(sm)

eh = endTime//60
em = endTime%60
if eh<10:
    eh = '0'+str(eh)
if em<10:
    em = '0'+str(em)
end  = str(eh)+':'+str(em)
print(start+' ~ '+end)



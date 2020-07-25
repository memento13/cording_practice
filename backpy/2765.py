import sys


pi = 3.1415927
result = []

def func(d,r,t):
    distance = d*r*pi
    avg = d/(time/(60*60))
    result.append([distance,avg])

def funcPrint():
    rlen = len(result)
    for i in range(rlen):
        print("Trip #%d : %.2f %.2f" %( i, result[i][0],result[i][1]))

while(True):
    diameter,rev,time = map(float,sys.stdin.readline().split())
    if rev == 0:
        break
    func(diameter,rev,time)

funcPrint()
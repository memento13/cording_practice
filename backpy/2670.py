import sys

n = int(sys.stdin.readline())
numlist = []

for i in range(n):
    numlist.append(float(sys.stdin.readline()))

maxnum = max(numlist)
for i in range(1,n):
    temp = numlist[i-1]*numlist[i]
    if temp > numlist[i]:
        numlist[i] = temp
    if maxnum < numlist[i]:
        maxnum = numlist[i]

print("%.3f"%maxnum)
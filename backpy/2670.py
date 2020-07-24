import sys

n = int(sys.stdin.readline())
numlist = []

for i in range(n):
    numlist.append(float(sys.stdin.readline()))

maxnum = numlist[0] 
priv = numlist[0]
for i in range(n):

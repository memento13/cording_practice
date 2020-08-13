import sys
testcase = int(sys.stdin.readline())
numlist = [0,1,1,1,2,2,3,4,5,7,9]+[0 for _ in range(90)]
for i in range(98):
    numlist[i+3] = numlist[i]+numlist[i+1]

for _ in range(testcase):
    N = int(sys.stdin.readline())
    print(numlist[N])
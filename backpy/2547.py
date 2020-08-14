import sys

testcase = int(sys.stdin.readline().strip())

def func():
    nt = sys.stdin.readline()
    N = int(sys.stdin.readline().strip())
    result = 0
    for _ in range(N):
        temp = int(sys.stdin.readline().strip())
        result += temp
    if(result%N==0):
        return "YES"
    else:
        return "NO"


for _ in range(testcase):
    print(func())
    
    
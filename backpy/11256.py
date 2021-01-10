import sys

def func():
    j,n = map(int,sys.stdin.readline().split())
    box = list()
    for _ in range(n):
        r,c = map(int,sys.stdin.readline().split())
        box.append(r*c)
    box.sort(reverse=True)
    result = 0
    for i in box:
        if j<=0:
            break
        else:
            j = j-i
            result+=1
    print(result)

testcase = int(sys.stdin.readline())
for _ in range(testcase):
    func()

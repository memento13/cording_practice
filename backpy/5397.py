import sys

testcase = int(sys.stdin.readline())

def func():
    pw = list(sys.stdin.readline().strip())
    left = []
    right = []
    for i in pw:
        if i=='<':
            if len(left) >0:
                right.append(left.pop())
            else:
                continue
        elif i ==">":
            if len(right)>0:
                left.append(right.pop())
            else:
                continue
        elif i =="-":
            if len(left):
                left.pop()
            else:
                continue
        else:
            left.append(i)
    left = ''.join(left)
    right = ''.join(right[::-1])
    print(left+right)

for _ in range(testcase):
    func()
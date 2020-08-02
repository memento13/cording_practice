import sys

N = int(sys.stdin.readline())

def VPS():
    qu = list(sys.stdin.readline().strip())
    left = 0
    right = 0
    for i in qu:
        if i == "(":
            left +=1
        else:
            right +=1
        if right>left:
            return "NO"
    if right == left:
        return "YES"
    return "NO"

for i in range(N):
    print(VPS())
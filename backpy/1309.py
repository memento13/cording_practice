import sys

possible = [0,3,7,17,41]


def func(n):
    if len(possible)-1>=n:
        return possible[n]
    else:
        possible.append(func(n-2)+(2*func(n-1)))

n = int(sys.stdin.readline())
if n>4:
    for i in range(5,n+1):
        possible.append((possible[i-2]+(2*possible[i-1]))%9901)

print(possible[n]%9901)

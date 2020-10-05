import sys

def LineTest(n):
    n = n+1
    result = 0
    slope = set()
    for i in range(1,n):
        for j in range(1,n):
            if i==j:
                continue
            temp = i/j
            if (temp) in slope:
                continue
            else:
                slope.add(temp)
                result+=1
    return result+3

c = int(sys.stdin.readline())
for i in range(c):
    print(LineTest(int(sys.stdin.readline())))
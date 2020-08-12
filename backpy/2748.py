import sys

F = [0,1]

def fiv(i):
    global F
    if i<len(F):
        return F[i]
    else:
        temp = fiv(i-1)+fiv(i-2)
        F.append(temp)
        return temp

n = int(sys.stdin.readline())

print(fiv(n))
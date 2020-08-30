import sys

fivlist = [1,1,2,3,5,8,13]
def fiv(i):
    if i<=len(fivlist):
        return fivlist[i-1]
    else:
        temp = fiv(i-1)+fiv(i-2)
        fivlist.append(temp)
        return temp

N = int(sys.stdin.readline())
print(fiv(N))
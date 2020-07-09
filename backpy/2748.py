F = [0,0]

def fiv(i):
    if i<len(F)-1:
        return F[i]
    else:
        temp = int(fiv(i-1)+fiv(i-2))
        F.append(temp)
        return

n = int(input())
fiv(n)
print(F[n])
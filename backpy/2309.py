import sys

p = []
for i in range(9):
    p.append(int(sys.stdin.readline()))

total = sum(p)
spy1 = 0
spy2 = 0
for i in range(8):
    for j in range(i+1,9):
        if total -(p[i]+p[j])==100:
            spy1 = p[i]
            spy2 = p[j]

p.remove(spy1)
p.remove(spy2)
p.sort()
for i in p:
    print(i)
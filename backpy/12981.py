import sys

r,g,b = map(int,sys.stdin.readline().split())

mi = min(r,g,b)
result = mi
if r-mi>0:
    result += (r-mi)//3
    if (r-mi)%3>0:
        result+=1

if g-mi>0:
    result += (g-mi)//3
    if (g-mi)%3>0:
        result+=1
if b-mi>0:
    result += (b-mi)//3
    if (b-mi)%3>0:
        result+=1

# for i in range(mi):
#     tr = r-i
#     tg = g-i
#     tb = b-i
#     tresult = i
#     tresult += (tr//3)
#     if tr%3>0:
#         tresult+=1
#     tresult += (tg//3)
#     if tg%3>0:
#         tresult+=1
#     tresult += (tb//3)
#     if tb%3>0:
#         tresult+=1
#     result = min(result,tresult)

for i in range(max(r,g,b)):
    tr = r-i
    tg = g-i
    tb = b-i
    tresult = i
    if tr<0:
        tr = 0
    if tb<0:
        tb = 0
    if tg<0:
        tg = 0
    tresult += (tr//3)
    if tr%3>0:
        tresult+=1
    tresult += (tg//3)
    if tg%3>0:
        tresult+=1
    tresult += (tb//3)
    if tb%3>0:
        tresult+=1
    result = min(result,tresult)

print(result)
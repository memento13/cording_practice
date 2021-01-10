import sys

ALL = 19*19
a,b = map(int,sys.stdin.readline().split())
cards1 = []
cards2 = []
for i in range(1,11):
    if i==a:
        continue
    cards1.append(i)
for i in range(1,11):
    if i==b:
        continue
    cards2.append(i)

pair = False
if a==b:
    pair = True

if pair:
    result = ((ALL-(10-a))/ALL)

else:
    lastnum = (a+b)%10
    win = 0
    for i in cards1:
        for j in cards2:
            if i==j:
                continue
            elif (i+j)%10<lastnum:
                win+=1
    result = (win/ALL)
print("%.3f" % result)



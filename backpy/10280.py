import sys

n,p = map(int,sys.stdin.readline().split())
plist=[]
for i in range(n):
    cal,name = map(str,sys.stdin.readline().split())
    cal = int(cal)
    plist.append(cal)
pcal=plist[p-1]
now=0
while True:
    if now>p:
        print("NO")
        break

    if not plist:
        print("NO")
        break
    plist.pop(0)
    now+=1

    if not plist:
        print("NO")
        break
    plist.pop()

    if not plist:
        print("NO")
        break
    temp = plist.pop(0)
    now+=1

    if pcal==temp:
        print("YES")
        break
    




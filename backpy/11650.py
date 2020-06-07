N =int(input())

a = list()
for i in range(N):
    x,y = map(int,input().split())
    b = (x,y)
    a.append(b)

a = sorted(a)
for i in a:
    for j in i:
        print(j,end=' ')
    print()


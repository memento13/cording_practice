N =int(input())

a = list()
for i in range(N):
    x,y = map(int,input().split())
    b = (x,y)
    a.append(b)

a = sorted(a, key = lambda x : (x[1],x[0]))
for i in a:
    for j in i:
        print(j,end=' ')
    print()


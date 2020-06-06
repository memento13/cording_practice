 
c = int(input())
a = list()

while c>0:
    temp = c%10
    a.append(temp)
    c=c//10

a.sort()
a.reverse()
for i in a:
    print(i,end='')

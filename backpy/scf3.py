import sys

n = int(sys.stdin.readline())

arr = list()
arrSize = [0]*n

for i in range(0,n):
    arr.append(list(str(sys.stdin.readline().strip())))

def func(size,x,y):
    if (x+size-1)>(n+1):
        return False
    if (y+size-1)>(n+1):
        return False
    try:
        for i in range(x,x+size):
            for j in range(y,y+size):
                if arr[j][i]=='0':
                    return False
    except:
        return False
    arrSize[size-1]+=1
    return True


for y in range(0,n):
    for x in range(0,n):
         i = 1
         while(func(i,x,y)):
             i+=1
             

num =1
total = sum(arrSize)
print("total: "+str(total))
if total==0:
    exit(0)
for i in arrSize:
    if i==0:
        break
    print("size["+str(num)+"]: "+str(i))
    num+=1

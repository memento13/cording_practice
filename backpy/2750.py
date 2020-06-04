N = int(input())

arr = []
for i in range(N):
    temp = int(input())
    arr.append(temp)
    
for i in range(N):
    for j in range(i,N):
        if arr[i]>arr[j]:
            temp = arr[i]
            arr[i]=arr[j]
            arr[j]=temp

for i in range(N):
    print(arr[i])

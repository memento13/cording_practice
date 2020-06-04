N = int(input())

arr = []
for i in range(N):
    temp = int(input())
    arr.append(temp)
    
arr.sort()

for i in range(N):
    print(arr[i])

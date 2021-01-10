import sys

testcase = int(sys.stdin.readline())
arr0 = [1,0,1,1]
arr1 = [0,1,1,2]
def fib(n):
    global arr0
    global arr1
    if len(arr0)-1<n:
        for i in range(len(arr0),n+1):
            arr0.append(arr0[i-2]+arr0[i-1])
            arr1.append(arr1[i-2]+arr1[i-1])
        print(str(arr0[n])+" "+str(arr1[n]))
    else:
        print(str(arr0[n])+" "+str(arr1[n]))
    return


for _ in range(testcase):
    temp = int(sys.stdin.readline())
    fib(temp)

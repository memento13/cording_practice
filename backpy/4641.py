import sys

def func(li):
    result = 0
    for i in li:
        if li.count(i*2)>0:
            result  += 1
    return (result)


while True:
    li = list(map(int,sys.stdin.readline().split()))
    if li.count(-1)>0:
        break
    li.remove(0)
    print(func(li))



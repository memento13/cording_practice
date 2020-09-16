import sys

A,B = map(int,sys.stdin.readline().split())

list = []
num = 1
while True:
    if len(list)>=B:
        break
    temp = [num]*num
    list = list+temp
    num +=1

list = list[A-1:B]
print(sum(list))
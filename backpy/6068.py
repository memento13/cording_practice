import sys

n = int(sys.stdin.readline())
todo = []
for _ in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    todo.append(temp)

todo = sorted(todo,key= lambda x :(-x[1],x[0]))
nowtime = todo[0][1]
for i in todo:
    if i[1]<nowtime:
        nowtime = i[1]
    nowtime = nowtime-i[0]
if nowtime<0:
    nowtime = -1
print(nowtime)
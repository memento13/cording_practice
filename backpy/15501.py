import sys

n = int(sys.stdin.readline())
source = list(map(int,sys.stdin.readline().split()))
puzzle = list(map(int,sys.stdin.readline().split()))

standard = source[0]
point = puzzle.index(standard)

if source[1]==puzzle[point+1%n]:
    flag = True # 뒤집기를 하지 않은 경우
else:
    flag = False #뒤집은 경우

if flag==True:
    for s in source:
        if not s==puzzle[point]:
            print('bad puzzle')
            exit(0)
        point+=1
        if point==n:
            point=0
else:
    for s in source:
        if not s==puzzle[point]:
            print('bad puzzle')
            exit(0)
        point-=1
        if point<0:
            point=n-1
print('good puzzle')


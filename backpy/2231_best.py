'''
최소 생성자 찾기
something
'''

import sys
num = int(sys.stdin.readline())

def sum_seperate(x):
    return sum([int(i) for i in str(x)])+x

for i in range(num-9*len(str(num)),num,1):
    if i < 0:
        pass
    elif sum_seperate(i) == num:
        print(i)
        break
    elif i == num-1:
        print(0)
"""
def battle(i, j):
    stack = [(i, j)]
    visit[i][j] = True
    s = w = 0
    while stack:
        i, j = stack.pop()
        if grid[i][j] == 'v': w+= 1
        elif grid[i][j] == 'k': s+= 1
        for ni, nj in (i-1,j), (i+1,j), (i,j-1), (i,j+1):
            if grid[i][j] == "#" or visit[ni][nj]: continue
            visit[ni][nj] = True
            stack.append((ni,nj))
    if s > w: w = 0
    else: s = 0
    return s, w

n, m = map(int,input().split())
grid = [list(input()) for i in range(n)]
visit = [[False]*m for i in range(n)]
sheep = 0
wolf = 0
for i in range(n):
    for j in range(m):
        if visit[i][j]: continue
        if grid[i][j] == 'v' or grid[i][j] == 'k':
            s, w = battle(i, j)
            sheep+= s; wolf+= w
print(sheep, wolf)
"""
"""
a = [242, 256, 237, 223, 263, 81, 46]
print('A = ', a)

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
rc('font',family = font_name)

x_data = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']
plt.title('일주일간 유동 인구수 데이터', fontsize = 16)
plt.xlabel('요일', fontsize = 12)
plt.ylabel('유동 인구수', fontsize = 12)
plt.scatter(x_data, a)
plt.plot(x_data, a)
plt.show( )
"""
# import sys

# a,b = map(int,sys.stdin.readline().split())
# if a-b>0:
#     print(2*(a-b)//b)
# else:
#     print(-2*(a-b)//b)


# import sys
# keypad = [[1,2,3],[4,5,6],[7,8,9],[10,0,10]]
# def findIndex(a):
#     for i in range(4):
#         if a in keypad[i]:
#             return i,keypad[i].index(a)
# y,x = findIndex(0)
# print(x,y)
# temp = 'a'
# print(temp[-1])

# import sys

# keypad = [[1,2,3],[4,5,6],[7,8,9],[10,0,10]]
# print(max(keypad))
# K = [[-1., -1., -1.],[-1., 9., -1.], [-1., -1., -1.]]
import numpy as np
temp = 11
temp = temp//10
print(temp)
temp = temp//10
print(temp)

K = np.array([[-2, -1, 0],[-1, 1, 1], [0, 1, 2]])

print(sum(K[0:1,0:1]))
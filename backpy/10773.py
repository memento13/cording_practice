from collections import deque
from sys import stdin as st

K = int(st.readline())
num = deque()
for _ in range(K):
    temp = int(st.readline())
    if(temp == 0):
        num.pop()
    else:
        num.append(temp)
print(sum(num))
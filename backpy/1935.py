from collections import deque
from sys import stdin as st

N = int(st.readline())
num_list = [0]*26
formula = list(st.readline().strip())

for i in range(N):
    num_list[i] = int(st.readline())



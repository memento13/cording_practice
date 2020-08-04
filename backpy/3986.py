from sys import stdin as st

N = int(st.readline())
result = 0
for i in range(N):
    word = st.readline().strip()
    stack = []
    for j in word:
        if not stack or stack[-1]!= j:
            stack.append(j)
        else:
            stack.pop()
    if not stack:
        result +=1
print(result)
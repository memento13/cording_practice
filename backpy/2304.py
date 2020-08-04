from sys import stdin as st

N = int(st.readline())
pillar = []

for i in range(N):
    pillar.append(list(map(int,st.readline().split())))
pillar.sort()
pillar_max = max(pillar,key=lambda parameter_list: parameter_list[1])
H_start = pillar[0][1]
L_start = pillar[0][0]
result = 0

for i in pillar:
    if i[1]>=H_start:
        for _ in range(L_start,i[0]):
            result+=H_start
        L_start = i[0]
        H_start = i[1]
    if i[0]==pillar_max[0]:
        break

H_start = pillar[-1][1]
L_start = pillar[-1][0]
for i in reversed(pillar):
    if i[1]>=H_start:
        for _ in range(i[0],L_start):
            result+=H_start
        L_start = i[0]
        H_start = i[1]
    if i[0]==pillar_max[0]:
        break
result+=pillar_max[1]
print(result)
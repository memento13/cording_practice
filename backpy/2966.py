import sys

Adrian = ['A', 'B', 'C']
Bruno = ['B','A','B','C']
Goran = ['C', 'C', 'A', 'A', 'B', 'B']

N = int(sys.stdin.readline())
test = list(sys.stdin.readline().strip())

dic = {'Adrian':0,'Bruno':0,'Goran':0}
for i in range(N):
    if test[i]==Adrian[i%3]:
        dic['Adrian'] +=1
    if test [i] == Bruno[i%4]:
        dic['Bruno'] +=1
    if test[i]==Goran[i%6]:
        dic['Goran'] +=1

result = max(dic.values())
print(result)
for i in dic.keys():
    if result == dic[i]:
        print(i)
import sys

"""
n = int(sys.stdin.readline())
xi = list(map(int,sys.stdin.readline().split()))
xi = sorted(xi) # xi 정렬
result = 0
team = []
for i in xi:
    if i == 1: #원맨팀은 그냥 result+1
        result +=1
        continue
    if not team: #팀에 아무도 없는경우 그냥 넣음
        team.append(i)
        continue
    if len(team)+1 == min(team): #팀원 하나 들어가면 꽉찬상태
        result +=1 
        team.clear() #팀 비우기
        continue
    team.append(i) #팀원 자리가 2개 이상인 경우
if team: #팀이 꽉차진 않아도 일단 팀인 경우 result +1
    result +=1
print(result)
"""
n = int(input())
x = sorted(map(int,input().split()))
team = 0
i = 0
while i < n:
    team+= 1
    i+= x[i]
print(team)
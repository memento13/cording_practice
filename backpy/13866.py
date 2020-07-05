team = list(map(int, input().split()))
team.sort()
result = (team[1]+team[2])-(team[0]+team[3])
print(abs(result))

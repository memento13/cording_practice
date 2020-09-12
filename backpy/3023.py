import sys

R,C = map(int,sys.stdin.readline().split())

blueprint = []
for i in range(R):
    blueprint.append(list(sys.stdin.readline().strip()))

card=[]
for i in range(R):
    card.append(blueprint[i]+list(reversed(blueprint[i])))
for i in range(R-1,-1,-1):
    card.append(blueprint[i]+list(reversed(blueprint[i])))

aR,bC = map(int,sys.stdin.readline().split())
aR=aR-1
bC=bC-1
if card[aR][bC] == '#':
    card[aR][bC] = '.'
else:
    card[aR][bC] = '#'

for i in card:
    print(''.join(i))





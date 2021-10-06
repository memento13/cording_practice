import sys

N,M,H = map(int, sys.stdin.readline().split())

town = list()

for _ in range(N):
    town.append(list(map(int,sys.stdin.readline().split())))

home = [(x,y) for x in range(N) for y in range(N) if town[y][x]==1]
max_milk = 0
def trip(x,y,hp,milk,drank,prex,prey):
    
    if( x<0 or x>=N):
        return
    if(y<0 or y>=N):
        return
    spot = town[y][x]

    # 집인경우
    if(spot==1):
        global max_milk
        max_milk = max(milk,max_milk)
        return
    
    # 마시지 않은 우유인 경우
    if(spot==2 and (x,y) not in drank):
        hp += H
        milk += 1
        drank.append((x,y))
    
    # 체력hp가 0인경우
    if (hp==0):
        return
    
    # 다음 점으로 이동
    # 하(.+)상(.-)좌(-.)우(.+)
    if not (x==prex and y+1==prey):
        trip(x,y+1,hp-1,milk,drank,x,y)
    if not (x==prex and y-1==prey):
        trip(x,y-1,hp-1,milk,drank,x,y)
    if not (x-1==prex and y==prey):
        trip(x-1,y,hp-1,milk,drank,x,y)
    if not (x+1==prex and y==prey):
        trip(x+1,y,hp-1,milk,drank,x,y)
    

trip(home[0][0],home[0][1]+1,M-1,0,[],home[0][0],home[0][1])
trip(home[0][0],home[0][1]-1,M-1,0,[],home[0][0],home[0][1])
trip(home[0][0]-1,home[0][1],M-1,0,[],home[0][0],home[0][1])
trip(home[0][0]+1,home[0][1],M-1,0,[],home[0][0],home[0][1])


print(max_milk)
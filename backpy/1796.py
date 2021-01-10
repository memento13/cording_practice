# fail
import sys

s = list(sys.stdin.readline().strip())
sort_s = sorted(s)
visited = [True]*len(s)

def left(visit,li,answer):
    li.reverse()
    visit.reverse()
    now = 0
    flag = False
    for i in range(len(li)):
        if li[i]== answer and visit[i]:
            flag = True
            break
        now+=1
    if flag:
        return now
    else:
        return 1000

def right(visit,li,answer):
    now = 0
    flag = False
    for i in range(len(li)):
        if li[i]== answer and visit[i]:
            flag=True
            break
        now+=1
    if flag:
        return now
    else:
        return 1000

result = 0
now = 0
end = len(s)
for i in sort_s:
    l = left(visited[0:now+1],s[0:now+1],i)
    r = right(visited[now:end],s[now:end],i)

    if l<r:
        now-=l
        visited[now] = False
        result+=(l+1)
    elif r<l:
        now+=r
        visited[now] = False
        result+=(r+1)
    print(now,result)

print(result)
# 01234
# acbbc
# abbcc

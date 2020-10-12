import sys

time = list(map(str,sys.stdin.readline().strip().split(':')))
h = int(time[0])
m = int(time[1])

keypad = [[1,2,3],[4,5,6],[7,8,9],[10,0,10]]

effort_min = ['HH','MM',9999]

def findIndex(a):
    for i in range(4):
        if a in keypad[i]:
            return keypad[i].index(a),i

def func(effort,hh,mm,case):
    global effort_min
    if case ==2 and int(hh)%24!=h: #시 안맞을떄
        return
    elif case ==4:
        if int(hh)%24==h and int(mm)%60 == m: #시,분 맞을때
            if effort_min[2]>effort:
                effort_min = [hh,mm,effort]
        return
    else:
        if case<2:
            temp = int(hh[-1])
            nowx,nowy = findIndex(temp)
            for i in range(10):
                nextx,nexty = findIndex(i)
                nowTonext = abs(nextx-nowx)+abs(nexty-nowy)
                func(effort+nowTonext,hh+str(i),mm,case+1)
        else:
            if mm == '':
                temp = int(hh[-1])
                nowx,nowy = findIndex(temp)
                for i in range(10):
                    nextx,nexty = findIndex(i)
                    nowTonext = abs(nextx-nowx)+abs(nexty-nowy)
                    func(effort+nowTonext,hh,str(i),case+1)
            else:
                temp = int(mm[-1])
                nowx,nowy = findIndex(temp)
                for i in range(10):
                    nextx,nexty = findIndex(i)
                    nowTonext = abs(nextx-nowx)+abs(nexty-nowy)
                    func(effort+nowTonext,hh,mm+str(i),case+1)
for i in range(10):
    func(0,str(i),'',1)
print(effort_min[0]+':'+effort_min[1])
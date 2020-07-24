import sys

case = []

def PrintCase():
    for i in range(len(case)):
        print("Case ",(i+1),": ",case[i],sep="")

def ResultSave(L,P,V):
    if V%P>L:
        temp = L
    else:
        temp = V%P
    case.append(((V//P)*L)+temp)

while(True):
    L,P,V = map(int,sys.stdin.readline().split())
    if(L+P+V==0):
        break
    ResultSave(L,P,V)

PrintCase()
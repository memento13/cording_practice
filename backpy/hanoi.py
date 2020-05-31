def move(start,to):
    print(start+" "+to)

def hanoi(N,start,to,via):
    if(N==1):
        move(start,to)
    else:
        hanoi(N-1,start,via,to)
        move(start,to)
        hanoi(N-1,via,to,start)

a=input()
a=int(a)
print(2**a - 1)
hanoi(a,'1','3','2')
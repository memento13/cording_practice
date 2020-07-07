N = int(input())

def func(side,time,x,y):
    for i in range(side*2):
        if time==N:
            print(x,y)
            return
        else:
            time = time+1
            if side%2==1:
                if i<side:
                    y=y+1
                else:
                    x=x+1
            else:
                if i<side:
                    y=y-1
                else:
                    x=x-1
    side = side+1
    func(side,time,x,y)

func(1,0,0,0)
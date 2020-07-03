n = int(input())
# step = list()
count = 0

def func(i,penalty):
    global count
    penalty -=1
    if i==n:
        # print(''.join(map(str,step)))
        count = count+1
        return
    elif i>n:
        return
    else:
        #step.append(1)
        func(i+1,penalty)
        #step.pop()

        #step.append(2)
        func(i+2,penalty)
        #step.pop()

        if penalty<=0:
            penalty = 3
            #step.append(3)
            func(i+3,penalty)
            #step.pop()
func(0,0)
print(count)
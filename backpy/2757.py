
RC_list = list()
result_list = []
def func_input():
    while True:
        RnCm = input()
        nCm = RnCm[1:]
        C = nCm.find('C')
        n = nCm[:C]
        m = nCm[C+1:]
        if(int(n)==0 and int(m)==0):
            break
        else:
            temp = [m,n]
            RC_list.append(temp)
result = ''
def convert(n):
    T = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
    if n<27:    
        result = result+T[n]
    else:
        q,r = divmod(n,26)
        
    q,r = divmod(n,26)
    if q ==0:
        return T[r]
    else:
        return convert(q)+T[r]


w = input()
w = int(w)
print(convert(w))


# def trans():

# func_input()
# print(RC_list)



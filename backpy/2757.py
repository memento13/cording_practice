
RC_list = list()


def convert(n):
    T = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"

    q,r = divmod(n,26)
    if q ==0:
        return T[r-1]
    else:
        if r==0:
            q = q-1
            if q==0:
                return T[r-1]
        return convert(q)+T[r-1]

def func_input():
    while True:
        RnCm = input()
        nCm = RnCm[1:]
        C = nCm.find('C')
        n = nCm[:C]
        m = nCm[C+1:]
        m = int(m)
        if(int(n)==0 and int(m)==0):
            break
        else:
            temp = convert(m)+n
            RC_list.append(temp)

func_input()
for i in RC_list:
    print(i)



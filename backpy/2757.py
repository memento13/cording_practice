
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

def trans26(num):
    result = ''
    num = int(num)
    while num>26:
        if(num%26==0):
            temp = 'A'
        else:
            temp = chr(num%26+64)
        result = temp+result
        num = num//26
    if(num==26):
        temp = 'Z'
        result = result+temp
    elif num%26 != 0:
        temp = chr(num%26+64)
        result = result+temp
    return result


w = input()
print(trans26(w))


# def trans():

# func_input()
# print(RC_list)



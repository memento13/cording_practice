N = int(input())
global MAX,MIN
N_list = list(map(int,input().split()))
operator_list = list(map(int,input().split()))

def make_operator_dict(operator_list):
    operator_dict = dict()
    for i,c in enumerate(operator_list):
        operator_dict[i] = c
    return operator_dict

def calculator(i,num,result):
    if i==0:
        result = result +num
        return result
    if i==1:
        result = result -num
        return result
    if i==2:
        result = result *num
        return result
    if i==3:
        if num<0:
            result = -1*(-result//abs(num))
        else:
            result = result // num
        return result

operator_dict = make_operator_dict(operator_dict)
result_list = list()
        
def cal(N_list, operator_dict):
    print(N_list,operator_dict)
    if len(N_list)==1:
        result_list.append(N_list[0])
        return 0
    else:
        result = N_list.pop(0)
        
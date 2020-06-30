N = int(input())
N_list = list(map(int,input().split()))
plus, minus, multiple, division = map(int, input().split())
operator_list = list()
operation_list += [1] * plus
operation_list += [2] * minus
operation_list += [3] * multiple
operation_list += [4] * division


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

operator_dict = make_operator_dict(operator_list)
result_list = list()
        
def cal(N_list, operator_dict):
    print(N_list,operator_dict)
    if len(N_list)==1:
        result_list.append(N_list[0])
        return 0
    else:
        result = N_list.pop(0)
        temp = N_list[0]
        for key,value in operator_dict.items():
            if value == 0:
                continue
            else:

        
N = int(input())
N_list = list(map(int,input().split()))
plus, minus, multiple, division = map(int, input().split())
result_list = list()
operator_list = list()
operator_list += [1] * plus
operator_list += [2] * minus
operator_list += [3] * multiple
operator_list += [4] * division


def calculator(i,num,result):
    if i==0:
        result = result +num
        return result
    elif i==1:
        result = result -num
        return result
    elif i==2:
        result = result *num
        return result
    elif i==3:
        if num<0:
            result = -1*(-result//abs(num))
        else:
            result = result // num
        return result

def func(i,result):
    if i==N:
        result_list.append(result)
        return
    else:
        temp_operator = operator_list.pop(0)
        result = calculator(temp_operator,N_list[i],result)
        for x in operator_list:
            func(i+1,result)
        operator_list.insert(0,temp_operator)

func(1,N_list[0])
result_list.sort()
min = result_list[0]
result_list.reverse()
max = result_list[0]
print(max)
print(min)
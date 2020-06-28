N = int(input())
global MAX,MIN
N_list = list(map(int,input().split()))
plus,minus,mul,div = map(int(input().split()))
operator_list = list()
operator_cheak = [True]*(N-1)
operator_list.append([0]*plus)
operator_list.append([1]*minus)
operator_list.append([2]*mul)
operator_list.append([3]*div)

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
            result = -1*(result//abs(num))
        else:
            result = result // num
        return result
        
def cal(i,result):
    if i==N-1:
        if result>MAX or MAX == None:
            MAX = result
        if result<MIN or MIN == None:
            MIN = result
        return
    
    for i in range(N-1):
        if operator_cheak[i]:
            operator_cheak[i] = False
            result = calculator(operator_list[i],N_list[i+1],result)
            operator_cheak[i] = True

cal(0,N_list[0])
print(MAX)
print(MIN)
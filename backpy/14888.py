N = int(input())
global result
global MAX,MIN
N_list = list(map(int,input().split()))
plus,minus,mul,div = map(int,input().splite())
operator_list = list()
operator_cheak = [True]*(N-1)
operator_list.append([0]*plus)
operator_list.append([1]*minus)
operator_list.append([2]*mul)
operator_list.append([3]*div)
result = N_list[0]

def calculator(i,num):
    if i==0:
        result = result +num
    if i==1:
        result = result -num
    if i==2:
        result = result *num
    if i==3:
        if Num<0:
            result = -1*(result//abs(Num))
        else:
            result = result // Num
        
def cal(i):
    if i==N-1:
        if result>MAX or MAX == None:
            MAX = result
        if result<MIN or MIN == None:
            MIN = result
        return
    
    for i in range(N-1):
        if operator_cheak[i]:
            


import sys 
def solution(s):
    cnt = len(s)
    
    s_arr = list(s)
    dic = {'{':'}', '[':']','(':')'}
    answer = 0
    for i in range(cnt):
        stack = list()
        flag = True
        for j in s_arr:
            if j in dic:
                stack.append(dic[j])
            else:
                if not stack:
                    flag = False
                    break
                elif stack[-1]!=j:
                    flag = False
                    break
                else:
                    stack.pop()
        if flag:
            answer +=1
        tmp = s_arr.pop()
        s_arr.insert(0,tmp)
                    
    return answer

N = sys.stdin.readline().strip()
print(solution(N))

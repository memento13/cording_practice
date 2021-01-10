import sys

testcase = int(sys.stdin.readline())

def test_input():
    k = int(sys.stdin.readline())
    students = list(map(int,sys.stdin.readline().split()))
    n = int(sys.stdin.readline())
    marathoners = []
    result = []
    cnt = 0
    for _ in range(n):
        temp = list(map(int,sys.stdin.readline().split()))
        if -1 in temp:
            continue
        tmp = [temp[0],temp[1]*60+temp[2]]
        marathoners.append(tmp)
    
    sorted_mts = sorted(marathoners,key= lambda x: (x[1]))
    flag = True
    for i in sorted_mts:
        if i[1]<361:
            if i[0] in students:
                if flag:
                    result.append(str(i[0]))
                    flag = False
                cnt+=1
    result.append(str(cnt))
    print(" ".join(result))

for _ in range(testcase):
    test_input()

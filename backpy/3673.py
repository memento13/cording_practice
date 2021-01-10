import sys


def func_input():
    d,n = map(int,sys.stdin.readline().split())
    temp = list(map(int,sys.stdin.readline().split()))
    total = 0
    cnt = 0
    dic = {0:1}
    for i in temp:
        total = (total+i)%d
        if total in dic.keys():
            cnt+=dic[total]
            dic[total]+=1
        else:
            dic[total] = 1

    print(cnt)


if __name__ == "__main__":
    testcase = int(sys.stdin.readline())
    for _ in range(testcase):
        func_input()
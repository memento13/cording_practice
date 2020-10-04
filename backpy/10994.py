import sys

def solution():
    N = int(input())
    temp = 4*N - 3
    sum = temp

    for i in range(temp):
        string = ''

        check = True
        if i % 2 == 1:
            check = False

        for j in range((temp - sum) // 2):
            if j % 2 == 0:
                string += '*'
            else:
                string += ' '

        for j in range(sum):
            if check:
                string += '*'
            else:
                string += ' '

        for j in range((temp - sum) // 2):
            if i % 2 == 1:
                if j % 2 == 1:
                    string += ' '
                else:
                    string += '*'
            else:
                if j % 2 == 0:
                    string += ' '
                else:
                    string += '*'

        if i + 1 >= temp // 2 + 1:
            sum += 2
        else:
            sum -= 2
        print(string)
solution()

N = int(sys.stdin.readline())
line = 4*N-3

def star(now):
    string=''
    if now==line:
        return
    if now%2==0:
        
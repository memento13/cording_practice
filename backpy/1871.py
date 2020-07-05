L = list()

def func():
    board2 = input()
    board2 = board2.split('-')

    front = list(board2[0])
    back = int(board2[1])
    result = 0

    for i in range(3):
        result += (int(ord(front[i]))-65)*(26**(2-i))

    result = back - result
    if result<=100:
        L.append("nice")
        print("nice")
    else:
        L.append("not nice")
        print("not nice")

N= int(input())
for i in range(N):
    func()
"""
for i in range(N):
    print(L[i])
"""
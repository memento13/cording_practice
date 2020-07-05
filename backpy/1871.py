def func(board2):
    board2 = board2.split('-')
    front = list(board2[0])
    back = int(board2[1])
    result = 0

    for i in range(3):
        result += (int(ord(front[i]))-65)*(26**(2-i))

    result = abs(back - result)
    if result<=100:
        print("nice")
    else:
        print("not nice")

N= int(input())
L = list()
for i in range(N):
    L.append(input())
for i in range(N):
    func(L[i])

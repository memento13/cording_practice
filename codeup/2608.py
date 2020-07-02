n = int(input())
vote = list()
def func(i):
    if i==n:
        print(''.join(vote))
        return
    else:
        vote.append('O')
        func(i+1)
        vote.pop()
        vote.append('X')
        func(i+1)
        vote.pop()

func(0)
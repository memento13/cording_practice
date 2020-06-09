N =int(input())
a = list()
for i in range(N):
    temp = input()
    a.append(temp)
a = list(set(a))
a = sorted(a, key=lambda item: (len(item),item))
for i in a:
    print(i)
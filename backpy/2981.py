import sys

n = int(sys.stdin.readline())
numbers = list()
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

result = list()
max_num = max(numbers)
first = numbers[0]
for i in range(2,max_num+1):
    value = first%i
    flag = True
    for j in numbers:
        if j%i != value:
            flag = False
            break
    if flag:
        result.append(str(i))
        
print(' '.join(result))
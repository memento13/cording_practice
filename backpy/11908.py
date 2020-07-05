n = int(input())
card = list(map(int, input().split()))
result = 0
for i in range(len(card)):
    result+=i
print(result)
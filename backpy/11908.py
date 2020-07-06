n = int(input())
card = list(map(int, input().split()))
card.sort()
result = 0
for i in range(len(card)-1):
    result+=card[i]
print(result)
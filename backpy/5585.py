import sys

value = int(sys.stdin.readline())
value = 1000-value
result = 0
coins = [500,100,50,10,5,1]
for i in coins:
    if value>=i:
        result+=(value//i)
        value=value%i

print(result)
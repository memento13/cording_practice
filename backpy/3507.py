import sys

n = int(sys.stdin.readline())
result = []

if n>=200:
    print(0)
    sys.exit(0)

for i in range(100):
    if n-i<100:
        result.append((i,n-i))

result = list(set(result))
print(len(result))
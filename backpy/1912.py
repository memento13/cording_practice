import sys

n = int(sys.stdin.readline())
verstappen = list(map(int,sys.stdin.readline().split()))
#Max max max SUPER MAX! Max max Super!

for i in range(1,n):
    verstappen[i] = max(verstappen[i], verstappen[i-1]+verstappen[i])
# 33 Max "SUPER" Verstappen
print(max(verstappen))

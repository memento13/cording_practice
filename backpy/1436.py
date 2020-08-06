import sys

N = int(sys.stdin.readline())

count = 0
num = 665
while(True):
    if str(num).find("666") != -1:
        count+=1
    if count == N:
        break
    num+=1
    

print(num)
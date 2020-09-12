import sys

mush = []
for i in range(10):
    mush.append(int(sys.stdin.readline()))

score = 0
for i in mush:
    if abs(100-score)>=abs(100-(i+score)):
        score = score+i
    else:
        break
print(score)

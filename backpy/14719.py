from sys import stdin as st

H,W = map(int,st.readline().split())
block = list(map(int, st.readline().split()))

def EmptyBlockCK(start,end):
    standard = min(block[start],block[end])
    water = 0
    for i in range(start+1,end):
        water +=(standard-block[i])
    return water

def FindBlockSide(start):
    temp = block[start]
    secondMax = start+1
    secondMaxValue = block[start+1]
    for i in range(start+1,W):
        if block[i] >= temp:
            return i
        if secondMaxValue<block[i]:
            secondMaxValue = block[i]
            secondMax = i
    return secondMax

result = 0
start = 0
while(start<W-1):
    end = FindBlockSide(start)
    result+=EmptyBlockCK(start,end)
    start = end

print(result)

import sys

N,K = map(int,sys.stdin.readline().split())
coin = []
for i in range(N):
    coin.append(int(sys.stdin.readline().strip()))

nowCoin = 0
coinIDX = len(coin)-1
while(True):
    if K<coin[coinIDX]:
        coinIDX -=1
    else:
        nowCoin = nowCoin+(K//coin[coinIDX])
        K = K%coin[coinIDX]
        if K==0:
            break
            
print(nowCoin)

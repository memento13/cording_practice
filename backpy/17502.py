import sys

N = int(sys.stdin.readline())
word = list(sys.stdin.readline().strip())
for i in range(N):
    if word[i]=='?':
        if word[-1+(-1*i)]=='?':
            word[i]='a'
        else:
            word[i]=word[-1+(-1*i)]
print(''.join(word))
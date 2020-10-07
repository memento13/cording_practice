import sys

n,m = map(int,sys.stdin.readline().split())

if m <=2:
    print("NEWBIE!")
elif m>2 and m<=n:
    print("OLDBIE!")
else:
    print("TLE!")
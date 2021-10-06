import sys


def gcd(a,b):
    if (b<a):
        a,b = b,a
    while(b!=0):
        a=a%b
        a,b = b,a
    return a

a,b = map(int,sys.stdin.readline().split())

gcd_num = gcd(a,b)
lcm_num = (a*b)//gcd_num
print(gcd_num)
print(lcm_num)
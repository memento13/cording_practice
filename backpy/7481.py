import sys

testcase = int(sys.stdin.readline())

def ATM(a,b,s,ac,bc):
    if s==0:
        return "{} {}".format(ac,bc)
    if s<a and s<b:
        return 'Impossible'
    ATM(a,b,s-b,ac,bc+1)
    ATM(a,b,s-a,ac+1,bc)


for _ in range(testcase):
    a,b,s = map(int,sys.stdin.readline().split())
    print(ATM(a,b,s,0,0))
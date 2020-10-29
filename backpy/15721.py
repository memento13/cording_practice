import sys

a = int(sys.stdin.readline())
t = int(sys.stdin.readline())
status = int(sys.stdin.readline())

st = [0,0]
now = 0
n = 2
while True:
    st[0]+=1
    if st[status]==t:
        print(now%a)
        exit(0)
    now+=1
    st[1] +=1
    if st[status]==t:
        print(now%a)
        exit(0)

    now+=1
    st[0]+=1
    if st[status]==t:
        print(now%a)
        exit(0)
    now+=1
    st[1] +=1
    if st[status]==t:
        print(now%a)
        exit(0)

    for _ in range(n):
        now+=1
        st[0]+=1
        if st[status]==t:
            print(now%a)
            exit(0)
    for _ in range(n):
        now+=1
        st[1]+=1
        if st[status]==t:
            print(now%a)
            exit(0)
    n+=1
    now+=1
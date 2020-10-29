import sys

w,p = map(int,sys.stdin.readline().split())
l = list(map(int,sys.stdin.readline().split()))
l.insert(0,0)
l.append(w)
result = set()
l_len = len(l)
for i in range(l_len):
    for j in range(i+1,l_len):
        result.add(l[j]-l[i])
# result.remove(0)
result = sorted(result)
print(' '.join('{}'.format(x)for x in result))

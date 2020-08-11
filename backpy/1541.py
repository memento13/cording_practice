import sys

formula = list(sys.stdin.readline().strip().split('-'))
for i in range(len(formula)):
    formula[i] = sum(list(map(int,formula[i].split('+'))))
result=0
for i in range(1,len(formula)):
    result +=formula[i]
print(formula[0]-result)


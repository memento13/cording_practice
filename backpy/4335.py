import sys
from copy import copy
numlist = [True]*11
temp = copy(numlist)
result = []
while True:
    num = int(sys.stdin.readline())
    if num ==0:
        break
    answer = sys.stdin.readline().strip()
    if answer=="too high":
        for i in range(num,11):
            temp[i]=False
        continue
    if answer=="too low":
        for i in range(0,num+1):
            temp[i]=False
        continue
    if answer=="right on":
        if temp[num]==False:
            print("Stan is dishonest")
        else:
            print("Stan may be honest")
        temp = copy(numlist)

import sys
from copy import copy
numlist = [0,1,2,3,4,5,6,7,8,9,10]
temp = copy(numlist)
result = []
while True:
    num = int(sys.stdin.readline())
    if num ==0:
        break
    answer = sys.stdin.readline().strip()
    if answer=="too high":
        temp = temp[:num]
        continue
    if answer=="too low":
        temp = temp[num+1:]
        continue
    if answer=="right on":
        if temp.count(num)==0:
            print("Stan is dishonest")
        else:
            print("Stan may be honest")
        temp = copy(numlist)

import sys
import math

h,y = map(int,sys.stdin.readline().split())
result = 0
def Acase(h,y):
    if y>=1:
        Start(int(h+((h/100)*5)),y-1)
    

def Bcase(h,y):
    if y>=3:
        Start(int(h+((h/100)*20)),y-3)
    else:
        return
def Ccase(h,y):
    if y>=5:
        Start(int(h+((h/100)*35)),y-5)
    else:
        return

def Start(h,y):
    global result
    if y==0:
        result = max(result,h)
        return
    Acase(h,y)
    Bcase(h,y)
    Ccase(h,y)

Start(h,y)
print(int(result))
    
import sys
import math

b,c = map(int,sys.stdin.readline().split())

result_plus = int(-b + math.sqrt(b**2-c))
result_minus = int(-b - math.sqrt(b**2-c))
if result_minus == result_plus:
    print(result_plus)
else:
    print('{} {}'.format(result_minus,result_plus))
import sys

num = int(sys.stdin.readline())
cars = list(map(int,sys.stdin.readline().split()))
print(cars.count(num))
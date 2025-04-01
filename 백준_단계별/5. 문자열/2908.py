import sys

input = lambda: sys.stdin.readline().rstrip()

numberStr1, numberStr2 = input().split(' ')

if int(numberStr1[::-1]) > int(numberStr2[::-1]):
    print(int(numberStr1[::-1]))
else:
    print(int(numberStr2[::-1]))

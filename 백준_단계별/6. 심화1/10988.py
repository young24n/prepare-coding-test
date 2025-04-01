import sys

input = lambda: sys.stdin.readline().rstrip()

str = list(input())

if str == str[::-1]:
    print('1')
else:
    print('0')
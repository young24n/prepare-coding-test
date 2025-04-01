import sys

input = lambda: sys.stdin.readline().rstrip()

try:
    while True:
        a, b = map(int, input().split(' '))
        print(str(a+b))
except ValueError:
    print('')
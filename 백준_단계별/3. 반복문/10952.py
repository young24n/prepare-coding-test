import sys

input = lambda: sys.stdin.readline().rstrip()

while True:
    a, b = map(int, input().split(' '))
    if a == 0 and b == 0:
        break
    print(str(a+b))
    
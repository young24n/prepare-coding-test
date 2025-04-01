import sys

input = lambda: sys.stdin.readline().rstrip()

cycle = int(input())
resultArr = []

for i in range(cycle):
    r, str = input().split(' ')
    for c in str:
        print(c * int(r), end='')
    print('')
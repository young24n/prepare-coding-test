import sys

input = lambda: sys.stdin.readline().rstrip()

size, target = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))

for i in arr:
    if i < target:
        print(i, end=' ')


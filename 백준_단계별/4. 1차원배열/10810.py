import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split(' '))

arr = [0] * n

for i in range(m):
    first, end, ball = map(int, input().split(' '))
    for j in range(first-1, end):
        arr.pop(j)
        arr.insert(j, ball)

for i in arr:
    print(i)

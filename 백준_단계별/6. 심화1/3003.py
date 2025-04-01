import sys

input = lambda: sys.stdin.readline().rstrip()

white = list(map(int, input().split(' ')))

need = [1, 1, 2, 2, 2, 8]

for n in [x - y for x, y in zip(need, white)]:
    print(n, end=' ')
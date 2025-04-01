import sys

input = lambda: sys.stdin.readline().rstrip()

size = int(input())
arr = list(map(int, input().split(' ')))

print(min(arr),max(arr))
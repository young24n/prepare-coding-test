import sys

# 파이썬에는 적합하지 않은 문제 같은데

input = lambda: sys.stdin.readline().rstrip()

size = int(input())

arr = list(map(int, input().split(' ')))

need = int(input())

print(arr.count(need))
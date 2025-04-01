import sys

input = lambda: sys.stdin.readline().rstrip()

size = int(input())
scores = list(map(int, input().split(' ')))
totalScore = 0


for i in scores:
    totalScore += i

print(totalScore / max(scores) * 100 / size)

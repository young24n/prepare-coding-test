import sys

input = lambda: sys.stdin.readline().rstrip()

stack = 0
scores = []


for i in range(10):
    scores.append(int(input()) % 42)

print(len(set(scores)))
import sys

input = lambda: sys.stdin.readline().rstrip()

str = input().split(' ')
counter = 0


for i in str:
    if len(i) > 0:
        counter += 1

print(counter)
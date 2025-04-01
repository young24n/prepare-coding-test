import sys

input = lambda: sys.stdin.readline().rstrip()

arr = []
result = []

for i in range(28):
    arr.append(int(input()))

arr.sort()

for i in range(1,31):
    if arr.count(i) == 0:
        result.append(i)

result.sort()

for i in result:
    print(i)
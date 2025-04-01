import sys

input = lambda: sys.stdin.readline().rstrip()

a, b = map(int, input().split(' '))

arr = []

for i in range(1, b+1):
    for j in range(i):
        arr.append(i)

sum = 0
for i in range(a-1,b):
    sum += arr[i]

print(sum)
import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split(' '))

arr = []
for i in range(1,n+1):
    arr.append(i)

for i in range(m):
    start, end = map(int, input().split(' '))
    arr[start-1:end] = reversed(arr[start-1:end])

for i in arr:
    print(i)
import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split(' '))

arr = []
for i in range(1, n+1):
    arr.append(i)

for i in range(m):
    case1, case2 = map(int, input().split(' '))
    temp = arr [case1-1]
    arr[case1-1] = arr[case2-1]
    arr[case2-1] = temp

for i in arr:
    print(i, end=' ')
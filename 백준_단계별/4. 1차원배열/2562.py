import sys

input = lambda: sys.stdin.readline().rstrip()

arr = []

for i in range(9):
    arr.append(int(input()))

print(max(arr))
print(arr.index(max(arr))+1)
import sys

input = lambda: sys.stdin.readline().rstrip()

size = int(input())

result = []

for i in range(size):
    string = "".join(input().split())
    unique = list(set(string))
    temp = [string.count(c) for c in unique]

    max_val = max(temp)
    count = temp.count(max_val)
    if count > 1:
        result.append('?')
    else:
        result.append(unique[temp.index(max_val)])

for i in result:
    print(i)
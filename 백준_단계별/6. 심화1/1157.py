import sys

input = lambda: sys.stdin.readline().rstrip()

str = list(input().upper())
result = []
unique = list(set(str))

for c in unique:
    result.append(str.count(c))

if result.count(max(result)) > 1:
    print('?')
else:
    print(unique[result.index(max(result))])
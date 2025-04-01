import sys

input = lambda: sys.stdin.readline().rstrip()

testCase = int(input())

strings = []

for i in range(testCase):
    strings.append(input())

for str in strings:
    print(str[0]+str[len(str)-1])

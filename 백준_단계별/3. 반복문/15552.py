import sys

input = lambda: sys.stdin.readline().rstrip()

testCase = int(input())

for i in range(testCase):
    a, b = map(int, input().split(' '))
    print(a+b)
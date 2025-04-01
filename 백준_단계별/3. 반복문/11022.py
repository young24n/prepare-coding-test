import sys

input = lambda: sys.stdin.readline().rstrip()

testCase = int(input())

for i in range(1, testCase+1):
    a, b = map(int, input().split(' '))
    print('Case #' + str(i) + ': ' + str(a) + ' + ' +  str(b) + ' = ' + str(a+b))
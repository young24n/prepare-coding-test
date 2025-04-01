import sys

input = lambda: sys.stdin.readline().rstrip()

num = int(input())

for i in range(1, num*2-2, 2):
    print((' ' * (num-int(i/2)-1)) + ('*' * (i)))

for i in range(num*2-1, 0, -2):
    print((' ' * (num-int(i/2)-1)) + ('*' * (i)))
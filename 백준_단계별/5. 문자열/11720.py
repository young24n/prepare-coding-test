import sys

input = lambda: sys.stdin.readline().rstrip()

length = int(input()) # ㅋㅋ

numberStr = input()
sum = 0


for i in numberStr:
    sum += int(i)

print(sum)
import sys

input = lambda: sys.stdin.readline().rstrip()

texts = ['c=', 'c-', 'dz=','d-', 'lj', 'nj', 's=', 'z=']

str = input()
sumWord = 0
for s in texts:
    sumWord -= str.count(s)

sumWord += len(str)
print(sumWord)
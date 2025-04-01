import sys

input = lambda: sys.stdin.readline().rstrip()

str = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for alphabetIndex, char in enumerate(alphabet, start=0):
    for index, j in enumerate(str, start=0):
        if char == j:
            print(index, end=' ')
            break
        elif index == len(str)-1:
            print('-1', end=' ')
            break
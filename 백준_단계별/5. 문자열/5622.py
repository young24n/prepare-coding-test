import sys

input = lambda: sys.stdin.readline().rstrip()

text = list(input())

dials = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

sec = 0

for c in text:
    for index, dial in enumerate(dials, start=3):
        if c in dial:
            sec += index
            break

print(sec)

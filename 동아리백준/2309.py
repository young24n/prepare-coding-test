import sys

input = lambda: sys.stdin.readline().rstrip()

heights = []
totalHeight = 0
found = False

for i in range(9):
    hei = int(input())
    heights.append(hei)
    totalHeight += hei

for i in range(9):
    for j in range(8,0,-1):
        if (totalHeight - (heights[i] + heights[j])) == 100:
            removeValue1 = heights[j]
            removeValue2 = heights[i]
            heights.remove(removeValue1)
            heights.remove(removeValue2)
            found = True
            break
    if found:
        break

for c in sorted(heights):
    print(c, end=' ')
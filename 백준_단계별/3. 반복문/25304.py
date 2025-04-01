totalCost = int(input())
stuffNumber = int(input())

sum = 0

for i in range(stuffNumber):
    cost, count = map(int, input().split())
    sum += cost * count
if sum == totalCost:
    print('Yes')
else:
    print('No')
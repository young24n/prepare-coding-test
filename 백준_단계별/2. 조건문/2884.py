h, m = map(int, input().split(' '))

totalMin = h * 60 + m

resultMin = totalMin - 45
if resultMin < 0:
    resultMin = 24 * 60 - 45 + m
print(int(resultMin / 60),end=' ')
print(int(resultMin % 60))

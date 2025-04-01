h, m = map(int, input().split(' '))
cookTime = int(input())

totalMin = h * 60 + m

resultMin = totalMin + cookTime

if resultMin >= 24 * 60:
    resultMin = resultMin % (24 * 60)

print(resultMin // 60,end=' ')
print(resultMin % 60)

arr = list(map(int, input().split(' ')))

result = 0
for i in arr:
    if arr.count(i) == 3:
        result = 10000 + i * 1000
        break
    elif arr.count(i) == 2:
        result = 1000 + i * 100
        break
    else:
        result = max(arr) * 100

print(result)
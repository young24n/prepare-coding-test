# 진법 변환

# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)
# 첫째 줄에 B진법 수 N을 10진법으로 출력한다.
# N = 숫자, B = 진법
#---
# 파이썬에서는 int()를 이용한 10 진법 변환 방법이 존재한다 -> int(숫자, 진수) -> 10 진수
N, B = input().split(" ")

number = int(N, int(B))
print(number)
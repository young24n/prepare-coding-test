# 소수

# 첫번째 줄에 M 두번째 줄에 N이 주어진다.
# M ~ N에 있는 소수를 모두 찾아 소수들의 합과 최솟값인 소수를 찾아라 (M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.)

# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.
# 소수가 없다면 -1을 출력

# 직전 소수 찾기의 로직을 사용한다. 바깥쪽 반복문의 범위를 range로 바꾸고 입력값을 대상으로 한다.
# 반복문 마지막 if 문에서 소수를 count 하던 것에서 저장하는 것으로 바꾼다.
# 저장된 소수는 자동으로 정렬됨으로 출력할때 0번 index에 접근한다. 
# 출력전 prime 리스트의 길이가 0인지 확인하고 0이라면 -1을 출력하도록 한다
# 내부함수 sum()을 통해 prime 리스트의 총합을 구하고 출력한다.

# 시간 초과
# 아무래도 소수를 찾는 더 간단한 방법이 있는듯 하다. 내부 반복문을 손봐야할 것 같다.
# 이미 처리된 소수를 기억하면 좋을 것 같은데 -> 대상이 소수인지 판별하는거고 1씩 증가하기 때문에 연관성이 없는 듯
# 약수 리스트 크기가 2 넘어가면 바로 스킵 하도록 해보자 -> 정답!
 
range1 = int(input())
range2 = int(input())

prime = []

for n in range(range1, range2 + 1):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
        if len(factors) > 2:
            break
    if len(factors) == 2:
        prime.append(factors[1])

if len(prime) == 0:
    print('-1')
else:
    print(sum(prime))
    print(prime[0])
# 블랙잭
# 규칙은 블랙잭과 같다. 다만 카드의 값들이 공개되어있고 최대값은 21에서 입력값 M으로 바뀐다.

# 첫번째 줄에 카드의 갯수 N과 근접해야할 최대값 M이 공백을 기준으로 입력된다.
# 이때 카드 3장을 선택하여 입력값 M을 넘지 않으면서 최대한 가까운 값을 출력한다.

# 브루트포스 문제이니 모든 경우의 수를 확인 하면 될 듯 하다.
N, M = map(int, input().split(' '))

cards = list(map(int, input().split(' ')))

closeOne = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N): # 카드의 index가 겹치면 안된다.
            sum = cards[i] + cards[j] + cards[k] # 해당 인덱스의 합을 구함
            if sum <= M and sum > closeOne: # 조건 비교
                closeOne = sum

print(closeOne)
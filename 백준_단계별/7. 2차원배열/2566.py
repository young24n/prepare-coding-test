# 최댓값

# 9 * 9 바둑판 형태로 81개의 0 ~ 100 수가 각각 요소로 입력된다.
# 이 2차원 배열에서 가장 큰 수를 찾은 후 해당 숫자의 행과 열을 출력해라
# 같은 수가 있을 경우 하나의 위치만 표시하면 된다.

# 입력 값은 한줄에 9개의 요소가 9번 들어온다. 이를 그대로 리스트로 만들고 배열에 넣으면 2차원 리스트가 된다.
# maxValue라는 기준 변수를 만들어 완전 탐색을 통해 기준값과 요소를 비교하여 더 큰 값을 기준 값으로 갈아치운다.
# 그리고 행과 열을 저장하는 변수 또한 만들어 더 기준값이 변경될 때 현재 index의 값으로 변수를 변경한다.
# 해당 변수들을 출력한다.

import sys
input = lambda: sys.stdin.readline().rstrip()

array = []
maxValue = 0
row = 1 # if가 최대값이 변경될때만 +1이 됨 그래서 0, 0이 아닌 1, 1로 초기화
col = 1

for i in range(9):
    array.append(list(map(int, input().split(' '))))

for i_index, i in enumerate(array):
    for j_index, j in enumerate(i):
        if maxValue < j:
            maxValue = j 
            row = i_index+1
            col = j_index+1

print(maxValue)
print(row, col, sep=" ")

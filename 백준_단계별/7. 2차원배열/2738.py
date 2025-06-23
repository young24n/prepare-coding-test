# 행렬덧셈

# 첫번째 줄에 행렬 2개에 대한 크기 N, M(두 행렬의 크기는 N * M 이다.)이 공백을 기준으로 입력된다.
# 이후 각 행렬의 요소가 줄마다 입력 된다.
# N * M  크기의 행렬 2개를 모두 입력한 뒤 각 행렬의 위치에 해당하는 각 요소를 더한 새로운 행렬을 출력한다.

# N을 반복문에 이용해 배열을 생성한다. 
# 요소 M 갯수에 대해서는 요소를 입력을 받을 때 공백 기준으로 분리하여 리스트로 변환하면 된다.
# 새로운 2차원 배열을 만들어 2개의 행렬에 같은 위치에 있는 요소를 서로 더해 새로운 행렬을 만들어 출력한다.
import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split(' '))

array1 = []
array2 = []

for i in range(N):
    array1.append(list(map(int, input().split(' '))))

for j in range(N):
    array2.append(list(map(int, input().split(' '))))

# 두 리스트를 동시에 순회하며 같은 요소들을 튜플로 반환하는 zip 이용
# 2차원이니 두번 써야함
for arrA, arrB in zip(array1, array2):
    for x, y in zip(arrA, arrB):
        print(x + y ,"", end='')
    print()
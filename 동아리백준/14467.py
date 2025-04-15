# 소가 길을 건너간 이유1
# 소를 N번 관찰한다.
# 각 관찰마다 소의 번호 C(1 ~ 10)와 소의 위치 L(0 또는 1)을 한 줄에 입력 받는다.
# 관찰이 끝나고 각 소의 위치가 변한 횟수의 총합을 출력한다.

# 구현--
# N을 입력받는다.
# ' '을 구분자로 C(소의 번호)와 L(위치)을 입력 받는다.
# sol 1 - 소는 10마리가 끝이니 해당하는 각 배열을 준비한다. 조건문을 이용해 나온 번호에 따라 위치를 해당 배열에 넣는다.
# 각 배열모든 배열을 순회하며 배열 내부 값이 몇번 바뀌었는지 조건문으로 카운트한다.
# sol 2 - 배열 두개를 준비한다. 각각의 배열은 소의 번호와 위치를 저장하는 용도이다.
# 입력값이 들어올 때마다 각 배열에 저장한다.(번호와 위치 index가 같아짐) 
# 새로운 입력값이 들어오면 조건문으로 소의 번호 배열에서 해당 번호가 있는지 확인한다.
# + index() 메소드가 가장 가까운 인덱스만 보기때문에 C가 추가된 상태이면 해당 인덱스의 P값을 교체하는 것으로 변경
# ai 코드리뷰 -> 이런식이면 딕셔너리로 cowNumber:position 형태가 더 효율적이긴 함
# 번호가 있다면 해당 인덱스와 같은 위치를 가져와 현재 입력된 위치와 비교한다 값이 다르다면 카운트한다.
# 출력한다.
import sys

input = lambda: sys.stdin.readline().rstrip()

cowNum = []
position = []
count = 0

N = int(input())

for i in range(N):
    C, P = map(int, input().split(' '))
    if C in cowNum:
        if position[cowNum.index(C)] != P:
            count += 1
            position[cowNum.index(C)] = P
    else:
        cowNum.append(C)
        position.append(P)

print(count)
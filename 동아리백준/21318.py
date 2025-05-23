# 피아노체조
# 첫 번째 줄에 악보의 개수 N(1 ≤ N ≤ 100,000)이 주어진다.
# 두 번째 줄에 1번 악보부터 N번 악보까지의 난이도가 공백을 구분으로 주어진다.
# 세 번째 줄에 질문의 개수 Q(1 ≤ Q ≤ 100,000)이 주어진다.
# 다음 Q개의 줄에 각 줄마다 두 개의 정수 x, y(1 ≤ x ≤ y ≤ N)가 주어진다.
# x번부터 y번까지의 악보를 번호 순서대로 연주한다.
# i번 악보의 난이도가 i + 1번 악보의 난이도보다 높다면 실수를 한다. 
# ->(다음(i+1) 난이도가 지금(i) 난이도 보다 낮으면 실수) 단 마지막으로 연주하는 y번 악보에선 절대 실수하지 않는다.
# 각 Q에 따른 실수 횟수를 출력한다.

# N을 입력 받는다.
# 난이도를 N갯수 만큼 한줄에 공백을 구분하여 입력받는다.
# 질문 받을 횟수 Q를 입력받는다
# 순서(x,y)를 입력받는다.
# 순서 범위의 난이도를 추출한다. (인덱스 슬라이싱 이용한다.)
# 추출한 난이도를 순차적으로 비교한다.
# (현재값과 이전값을 순환할 때마다 저장하여 비교, 최초 이전값은 0으로 설정해 무조건 실수가 발생하지 않도록 설정)
# 실수가 발생할 경우 결과를 배열로 저장한다. 단 마지막 y번째는 예외처리한다.
# 이를 Q번 반복한다. 배열에 저장된 결과를 모두 출력한다.
#-----> 시간초과 for가 중접된게 문제인가? Q,N 범위가 크긴하네

# 누적값 알고리즘? 뭘 누적 시키는겨 
# 찾아보니깐 실수를 누적하라고

# 아 인덱스 구간별 실수가 발생하는 것을 저장해두고 누적시키면 되겠네
# 어떻게 구성할 것인지?

# 입력 받는 방식은 같음
# 처음 난이도가 입력된 순간 모든 구간에 대한 실수 발생 여부를 저장한다.(0 or 1) i > i+1
# 따로 생성된 값을 이용한다.
# xy 범위가 주어지면 해당 구간의 실수를 합하여 출력한다.
#------> 시간초과 찾아보니 합까지 전부 해놓으라고 한다.
# 1 ~ i번까지 실수를 모두 합을 해 각 i번째에 저장한다.
# 값을 구할때는 합을 저장한 리스트의 x번째와 y번째의 차를 구하면 해당 위치의 값을 구하게됨



import sys

input = lambda: sys.stdin.readline().rstrip()

N = input()
lv = list(map(int, input().split(' ')))
Q = int(input())

mistakes = []

for i in range(len(lv)-1):
    if lv[i] > lv[i+1]:
        mistakes.append(1)
    else:
        mistakes.append(0)

prefix_mistakes = [0] * (len(mistakes) + 1)
for i in range(len(mistakes)):
    prefix_mistakes[i + 1] = prefix_mistakes[i] + mistakes[i]

for _ in range(Q):
    x, y = map(int, input().split())
    print(prefix_mistakes[y - 1] - prefix_mistakes[x - 1])
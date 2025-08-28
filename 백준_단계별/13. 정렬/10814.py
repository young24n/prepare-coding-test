# 나이순 정렬

# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 
# 회원들을 나이가 증가하는 순으로, 
# 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

# 직전 문제와 마찬가지로 key와 튜플을 이용하면 된다. 
# key에 해당하는 함수 구성을 나이가 1순위, 
# 입력된 이름을 이용하여 해당 인덱스의 위치를 2순위로 구성하면 요구 조건을 충족할 것이다.
# lambda x: (x[0], user.find(x[1])) 아마 이런식으로 구성하면 될 것 같다. 
# x로 들어오는 인자는 예제와 같이 [[21, Junkyu], [21, Dohyun], [20, Sunyoung]]
# 이러한 형태로 저장하면 된다.

# find는 텍스트만 해당하고 리스트는 index를 이용해야 한다고 한다. userList.find(x[1]) -> userList.index(x[1])
# 접근 방식이 잘못되었다. 왜 이름만 따로 추출해서 찾는지?
# x를 그대로 이용해서 이름과 나이까지 비교하는게 더 간단하고 확실하다. userList.index(x)

# 시간초과 자료의 양이 그렇게 많지 않음에도(1 ≤ N ≤ 100,000) key에서 index로 접근하는 방식이 부담되었나 보다
# 최적화 할 방법이 있나? 
# 힌트를 좀 봤는데 값이 입력될 때 값을 들어온 순서를 id 처럼 추가로 삽입하여 저장시키는 것이다.
# 확실히 이 방법이면 index를 찾기위해 매번 전체 list를 순회할 필요도 없다. userList.index(x) -> x[2]

n = int(input())

userList = []

for id in range(n):
    age, name = input().split(' ')
    userList.append([int(age), name, id])

target = sorted(userList, key=lambda x: (x[0], x[2]))

for text in target:
    print(text[0], text[1])
# 그룹단어
# 첫째 줄에 단어의 개수 N이 들어온다. 
# N은 100보다 작거나 같은 자연수이다. 
# 둘째 줄부터 N개의 줄에 단어가 들어온다. 
# 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

# 그룹단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우
# ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, 
# kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 문자가 1개인 경우 index 관계없이 항상 연속적인 상태이다. 그렇기 때문에 그룹단어이다.
# 문자가 2개 이상부터는 index가 연속적이여야 그룹단어 상태이다.
#### 어떻게 구성할까
# N을 입력 받는다.
# 단어를 입력 받는다.
# 단어를 순회하다 이전과 다른 문자가 나모면 지나온 문자를 set을 통해 유니크하게 저장한다.
# 이때 순회하면서 항상 해당 문자가 set에 들어있는지 검증한다.
# 만약 set에 존재하는 문자가 단어를 순회하다 다시나오면 break통해 해당 단어를 넘어간다
# 모두 순회한다면 stack을 1 증가 시킨다.
# 이것을 N번 반복하여 결과를 저장한다. 그룹단어가 몇개인지 출력한다.

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

stack = 0
for i in range(N):
    word = input()
    changed = set()
    lastChar = ''
    isbreak = False
    for c in word:
        if lastChar != c:
            if c in changed:
                isbreak = True
                break
            changed.add(c)
        lastChar = c
    if not(isbreak):
        stack += 1

print(stack)
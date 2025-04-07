# 세로읽기 
# 한 줄의 단어는 글자들을 빈칸 없이 연속으로 나열해서 최대 15자를 이룰 수 있다.
# 줄의 개수는 5개로 고정되어 있다.
# 세로로 읽는 도중 빈칸이 나오면 세로로 다음 글자로 넘어간다.

# 문자열을 입력 5번 입력 받는다. 문자열들을 리스트로 변경하여 2차원 형태로 저장한다.
# 2차원 리스트 중 가장 길이가 긴 문자열을 기준으로 나머지 줄에 공백을 추가한다.    
# 2차원 리스트를 세로로 읽어간다.
# 반복문을 이용하여 세로로 읽어간 문자열을 리스트에 저장한다.
# 공백이 나올 경우 리스트 입력을 무시한다.
# 마지막으로 리스트를 join하여 출력한다.

import sys

input = lambda: sys.stdin.readline().rstrip()

arr = [list(input()) for _ in range(5)]
result = []

max_len = max(len(s) for s in arr)
for i in range(5):
    if len(arr[i]) < max_len:
        arr[i] += [''] *  (max_len - len(arr[i]))

for i in range(max_len):
    for j in range(5):
        if arr[j][i] != '':
            result.append(arr[j][i])

print(''.join(result))
# 수 정렬 2750
# 휴가철이라 해당 기간동안은 간단한 문제를 풀기로 했다.
# 자연수 N 만큼 수를 입력 받고 해당 수들을 오름차순으로 정렬하여 한 줄 씩 출력하면 된다.

# 자연수 N은 첫줄에 입력 되며 이후는 N만큼 숫자를 입력 받으면 된다.
# 이후 해당 수를 정렬하여 출력하면 된다.
sortList = []
ran = int(input())
for i in range(ran):
    sortList.append(int(input()))

sortList.sort()
for i in sortList:
    print(i)
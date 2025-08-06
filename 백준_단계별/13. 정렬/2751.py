# 수 정렬 2

# 수 정렬 문제와 같다 다만 자료의 크기가 매우 크기 때문에 코드를 그대로 사용하면 시간초과가 나온다.
 
# 정렬은 이미 Timsort를 사용하는 .sort()로 문제는 없다. 
# 다만 입력에 대한 반복문이 시간초과를 발생시킨다. 
# 자바의 경우 다른 정렬을 사용해야한다. 같은 문제인데 다른 문제점을 지닌점이 흥미롭다.

import sys
input = lambda: sys.stdin.readline().rstrip()

sortList = []
ran = int(input())
for i in range(ran):
    sortList.append(int(input()))

sortList.sort()
for i in sortList:
    print(i)
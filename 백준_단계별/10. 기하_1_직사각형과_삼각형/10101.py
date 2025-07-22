# 삼각형 외우기

# 삼각형의 세 각을 입력받은 다음
# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error를 출력하는 프로그램을 작성
# 총 3개의 줄에 걸쳐 삼각형의 각의 크기가 주어진다. 모든 정수는 0보다 크고, 180보다 작다.

# 흔한 구현 문제 위의 조건을 그대로 구현하면 된다.

A = int(input())
B = int(input())
C = int(input())

# 중복되는 구문이 조금 있다만 잘 작동한다.

if A == B and B == C and C == 60:
    print('Equilateral')
elif A + B + C == 180 and (A == B or B == C or A == C):
    print('Isosceles')
elif A + B + C == 180 and (A != B or B != C or A != C):
    print('Scalene')
elif A + B + C != 180:
    print('Error')

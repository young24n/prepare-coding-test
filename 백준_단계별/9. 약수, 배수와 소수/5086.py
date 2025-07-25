# 배수와 약수

# 두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성하시오.
# 상태는 총 3가지 이다.
# 첫 번째 숫자가 두 번째 숫자의 약수이다.
# 첫 번째 숫자가 두 번째 숫자의 배수이다.
# 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.

# (X)예제입력이 반복문 처럼 되어있지만 딱히 테스트 케이스를 입력 받는 횟수는 없다. 각각으로 보면 될 것 같다.
# B % A = 0 이면 약수
# A % B = 0 이면 배수
# 위 절차를 걸치고 나머지 또한 있다면 둘다 아닌것으로

# 테스트 케이스를 무한으로 입력 받고 0 0으로 종료를 입력받는 형태였다. 

while True:
    A, B = map(int, input().split(' '))

    if A == 0 and B == 0:
        break

    if 0 == B % A:
        print('factor')
    elif 0 == A % B:
        print('multiple')
    else:
        print('neither')
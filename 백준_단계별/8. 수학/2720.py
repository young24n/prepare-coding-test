# 세탁소 사장 동혁

# 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)의 개수를 구하는 프로그램을 작성
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
# 각 테스트 케이스는 거스름돈 C를 나타내는 정수 하나가 입력되며 C의 단위는 센트이다. (1달러 = 100센트) (1<=C<=500)

# 동전 갯수 구하기 문제의 달러 버전이다.
# 가장 큰 수의 동전부터 작은 동전까지 (%) 나머지와 (//) 몫을 구하는 연산을 한다.
# 나머지 값은 다음 동전에 대한 연산을 반복하고 몫은 동전 갯수로 출력하면 된다.
# 주의할 점은 한국 동전문제와 다르게 다뤄지는 값들이 소수점이 있다는 것

# 소수점을 다루는 문제이지만 나누는 값(동전들)과 달러(입력값 C)를 *100 하여 정수로 변환하여 다뤄도 상관없어 보인다.
# 우선 테스트 케이스 T에 대해 1회 입력 받는다.
# T 만큼 반복하는 반복문에 달러 값인 C에 대한 입력과 거스름돈을 구하는 로직을 넣는다.
# 거스름돈에 대한 로직은 아래로 구성되어있다.
# 1. 가장 큰 값인 쿼터 동전부터 달러를 연산하여 나머지와 몫을 구한다.
# 2. 몫은 해당 동전의 갯수로 저장하고 나머지 값은 다음으로 큰 동전 값으로 나눈다.
# 3. 가장 작은 페니까지 반복한다.
# 4. 입력, 출력 프레임은 별개로 판단되며 입력 출력을 반복하여도 상관 없는 것으로 보인다.

# 문제에 대한 표현을 착각했다. (Quarter, $0.25) <- 달러였다.
# 1달러 = 100센트라고 언급했으니 각각 25, 10, 5, 1이 맞는 값이다. 그대로 계산하지 않는다.

Quarter = 25
Dime = 10
Nickel = 5
Penny = 1

T = int(input())

for i in range(T):
    C = int(input())
    quotientQuar = C // Quarter
    remainderQuar = C % Quarter

    quotientDime = remainderQuar // Dime
    remainderDime = remainderQuar % Dime

    quotientNick = remainderDime // Nickel
    remainderNick = remainderDime % Nickel

    quotientPenny = remainderNick // Penny
    remainderPenny = remainderNick % Penny

    print(quotientQuar, quotientDime, quotientNick, quotientPenny)

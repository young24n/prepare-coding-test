# 소수 찾기

# 첫번째 라인에 입력된 숫자의 갯수 N이 주어진다.
# 두번째 라인에 공백 기준으로 N갯수 만큼의 숫자가 입력된다. 
# 입력된 숫자들이 소수인지 판단하고 몇개 인지 출력

# 여기서 말하는 소수는 약수로 1과 자기자신 뿐인 숫자를 말한다.

# 반복문을 이용해서 소수를 찾는다. 1 ~ n+1까지 반복시킨다. 
# 해당과정에서 나오는 약분 대상을 나머지 연산으로 약분을 찾아 list에 저장한다.
# list 는 반복문이 시작될 때마다 초기화된다.
# range를 이용해 1~n+1까지 반복하였기에 소수라면 list의 길이는 2이다.
# count를 통해 소수의 갯수를 저장한다.
# count를 출력한다.

N = int(input()) # 아마 배열의 크기를 지정하기 위한 입력이지만 파이썬에서는 동적이라 필요없는 파트 사용하려면 어떻게든 가능하지만 굳이?

numbers = map(int, input().split(' '))
count = 0

for n in numbers:
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(n)
    if len(factors) == 2:
        count += 1

print(count)    

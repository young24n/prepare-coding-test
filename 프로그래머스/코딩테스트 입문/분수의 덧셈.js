// 분수의 덧셈

// 문제 설명
// 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 
// 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

// // 분수 덧셈 공식을 이용하면 된다.
// 두 분모를 서로 곱하기 (denom1 * denom2) 공통 분모 생성
// 각 분자에 상대방의 분모를 곱한 값을 서로 더하기. (numer1 * denom2 + numer2 * denom1)

// 줄일 필요가 전혀 없는데

// 약분까지 해줘야 한다. 
// 분자 분모의 최대 공약수를 구해 나누어 주면 된다.
// 최대공약수는 소인수분해, 유클리드 호제로 구할 수 있다.
// 유클리드 호제의 논리적 증명은 알아서 찾아보고 사용방법은 다음과 같다
// 다음 두 수가 있다 48, 18 이 두 수의 최대공약수를 구하려면
// 두수를 나눈 나머지를 구한다. 48 % 18 = 12
// 여기서 나눈 수와 나머지를 또 나눈다. 18 % 12 = 6
// 나머지가 0이 될때까지 이를 반복한다. 12 % 6 = 0
// 최대공약수는 6이다.
// 반복문 혹은 재귀로 이를 구현하면 된다.

function solution(numer1, denom1, numer2, denom2) {
    let numer = numer1 * denom2 + numer2 * denom1;
    let denom = denom1 * denom2;
    const getGcd = (a, b) => (b === 0 ? a : getGcd(b, a % b));
    const gcd = getGcd(numer, denom);

    var answer = [numer / gcd, denom / gcd];
    return answer;
}
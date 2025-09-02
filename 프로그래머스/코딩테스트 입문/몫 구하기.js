// 두 수의 합 구하기와 같다. 문제 설명을 축약.
// 문제 설명

// 정수 num1, num2가 매개변수로 주어질 때, 
// num1을 num2로 나눈 몫을 return 하도록 solution 함수를 완성해주세요.

/**  
기본으로 제공되는 코드
function solution(num1, num2) {
    var answer = 0;
    return answer;
}
*/

// 충격 % 나머지 연산자는 있는데 몫 연산자가 없었다니..
// 이걸 대신 사용해야한다. Math.floor() 안에 있는 값을 내림처리 해줌

function solution(num1, num2) {
    var answer = num1 / num2;
    return Math.floor(answer);
}
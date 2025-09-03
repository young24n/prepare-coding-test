// 두 수의 나눗셈

// 문제 설명
// 정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 
// return 하도록 solution 함수를 완성해주세요.

// 제공 코드 
// function solution(num1, num2) {
//     var answer = 0;
//     return answer;
// }

// 값을 나눈 후 1000을 곱하고 정수 부분만 리턴하면 된다. 정수파트만 넘겨돌라했으니 소수점을 없애주자

function solution(num1, num2) {
    var answer = num1 / num2 * 1000;
    return Math.floor(answer);
}
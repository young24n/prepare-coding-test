// 정수 n이 매개변수로 주어질 때, 
// n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.

// N 이하의 값이 담긴 배열을 반환하면 된다. 단 짝수 없이
// 오히려 최빈값 문제보다 간단하다.
// N 만큼 반복문을 돌리고 그 인덱스를 저장하면된다. 해당 값이 홀수일때만
// 나머지 연산을 이용하면 쉽게 홀짝 구분이 가능하다.

function solution(n) {
    var answer = [];
    for(let i = 0; i <= n; i++) {
        if (i % 2 != 0) answer.push(i)
    }
    return answer;
}
// 문제 설명
// 정수 n이 주어질 때, 
// n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

// 내가 돌아왔다!
// 오랜만이니 조금 더 풀어야겠다.

// 1 ~ N까지의 짝수를 모두 합하면된다. 짝수는 2를 나눈 수에서 나머지가 0이 나오면 짝수다. 1이 나올경우 홀수

function solution(n) {
    var answer = 0;
    for (let i = 0; i <= n; i++) {
        if (i % 2 == 0) answer += i
    }
    return answer;
}
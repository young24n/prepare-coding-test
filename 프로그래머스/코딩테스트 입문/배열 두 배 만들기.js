// 배열 두 배 만들기

// 문제 설명
// 정수 배열 numbers가 매개변수로 주어집니다. 
// numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

// 파라미터가 배열로 주어진다. 
// 배열의 원소를 하나씩 탐색하여 새로운 배열을 반환하는 map을 이용하여 각 원소를 2 곱해주면 될 듯 하다.

function solution(numbers) {
    var answer = numbers.map((a => (a * 2))) // {} -> 코드 작성란 return 사용시 명시해야함, () or 생략 -> 표현식 결과가 암묵적으로 return 됨
    return answer;
}
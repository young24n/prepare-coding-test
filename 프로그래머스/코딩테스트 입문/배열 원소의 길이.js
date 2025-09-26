// 문제 설명
// 문자열 배열 strlist가 매개변수로 주어집니다. 
// strlist 각 원소의 길이를 담은 배열을 return하도록 solution 함수를 완성해주세요.

// 배열에 문자열이 담겨있는데 그 원소들을 숫자로 치환하여 새로운 배열을 만들면된다.
// 이런 경우는 map이 아주 유용하다.
// 특정 배열의 원소를 조정하여 새로운 배열을 반환한다.

function solution(strlist) {
    var answer = strlist.map(str => str.length) // str.length를 리턴해주고 있는데(return이 생략된 상태) return된 것들은 모두 하나의 배열에 담겨 변수에 담긴다.
    return answer;
}
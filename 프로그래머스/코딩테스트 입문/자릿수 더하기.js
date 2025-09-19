// 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 
// solution 함수를 완성해주세요

// N은 숫자이니 우선 문자열로 형변환 해준다.
// 각 자리수를 구하면서 배열로 변경하기 위해 split 사용
// 반복문, reduce, forEach 등등 순회할 수 있는 방식을 선택해서 각 자리수를 합산하면된다.

// parseInt()는 문자열로 된 부분에서 숫자(정수)만 뽑아서 변환해주는것이 특징이고, 
// Number()은 문자열 전체가 숫자일때 소수점까지 숫자타입으로 가져올 수 있다는것이다.

function solution(n) {
    var answer = String(n).split('').reduce((acc, crr) => acc + Number(crr), 0)
    return answer;
}
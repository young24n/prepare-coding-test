// 문제 설명
// 정수 배열 numbers가 매개변수로 주어집니다. 
// numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

// 모든 요소의 평균 = 모든 요소의 합 / 모든 요소의 수
// 안타깝게도 JS에서는 평균을 구해주는 내장 메서드가 없다.
// forEach, for in ~, for of ~, reduce 등등 마음에 드는걸 사용하면 된다.
// for in은 인덱스로 되니 배열에 직접 접근하도록 바꿔야함

// 참고 reduce 메서드
// const sum = numbers.reduce((acc, cur) => acc + cur, 0);
// acc: accumulator (누적값)
// cur: currentValue (현재값)
// 0: initialValue (초기값)

function solution(numbers) {
    var answer = 0;
    for (let num of numbers) {
        answer += num;
    }
    return answer / numbers.length;
}
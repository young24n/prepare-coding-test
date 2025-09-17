// 문제 설명
// 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. 
// num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.

// 반복문을 이용해서 주어진 배열을 하나씩 참조한다.
// 인덱스를 역순으로 할 필요는 없다. js에서는 넣는 순서를 반대로 하는 unshift가 있으니
// reverse 메서드가 있는데 이것은 원본 배열을 변경시킴으로 주의해야한다. 
// spread 연산자를 이용해 원본 변경없이 메서드 사용이 가능하다. -> [num_list...].reverse()

function solution(num_list) {
    var answer = [];
    for (let i = 0; i < num_list.length; i++) {
        answer.unshift(num_list[i])
    }
    return answer;
}
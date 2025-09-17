// 문자열 my_string이 매개변수로 주어집니다.
//  my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.


// split()으로 글자를 나눠 배열로 바꾸고 reverse를 써준다. 
// 다시 문자열로 바꾸기 위해 join()을 사용한다.

function solution(my_string) {
    var answer = my_string.split('').reverse();
    return answer;
}
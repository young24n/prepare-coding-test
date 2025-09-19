// 문제 설명
// 머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다.
// 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 
// 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.

// 머쓱이 키 h와 반애들 키 arr이 주어진다.
// arr에서 h보다 큰 놈들의 수를 구하면 된다.

// filter가 바로 생각났다 함수로 인자 넘겨주면 함수 조건대로 거른 후 새로운 배열을 반환한다.
// 해당 배열의 length만 추출하면 끝

function solution(array, height) {
    // 이렇게 해도 되는데 가독성 따지면 length 분리하는게 맞음 몇줄 늘어나더라도 
    // 코딩은 결국 남들 보여주고 협동하는 용도이니 남들의 가독성이 최우선 사항 버그 최적화 등등은 그 다음임
    var answer = array.filter(h => h > height).length 
    return answer;
}
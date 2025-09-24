// 문제 설명
// 사분면은 한 평면을 x축과 y축을 기준으로 나눈 네 부분입니다.
// 사분면은 아래와 같이 1부터 4까지 번호를매깁니다.

// dot[0]은 x좌표를, dot[1]은 y좌표를 나타냅니다.

// x,y의 음양에 따라 사분면을 표기하면된다. 
// 제한사항으로 원소가 0이 되지는 않기에 그부분은 걱정 안해도 된다.
// 조건문으로 구현하면 된다.


function solution(dot) {
    var answer = 0;
    if (dot[0] > 0 && dot[1] > 0) answer = 1 // 양양
    else if (dot[0] < 0 && dot[1] > 0) answer = 2 // 음양
    else if (dot[0] < 0 && dot[1] < 0) answer = 3 // 음음
    else if (dot[0] > 0 && dot[1] < 0) answer = 4 // 양음
    return answer;
}
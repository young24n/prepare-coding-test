# 너의 평점은 // 수학 문제는 왜 말을 빙빙 돌려서 하는게 패시브일까?

# 전공 평점 계산 프로그램
# 20 줄에 걸쳐 과목명, 학점, 등급(성적)이 공백을 구분으로 주어진다
# 전공평점을 출력한다 소수점 0.000001까지의(문제에서는 10^-4 이하) 오차는 정답으로 인정된다.
# 전공평점은 전공과목별 (학점 × 과목평점(성적))의 합을 학점의 총합으로 나눈 값이다.
# 과목중 P/F(Pass/Fail) 중 P에 해당하는 과목은 계산에서 제외한다.

# 한 줄에 데이터 3개가 들어온다 해당 정보를 각각 텍스트로 변수에 나눠 담는다.
# 우선 성적에 P가 있으면 그 과목을 스킵하도록 검증한다.
# 학점, 성적의 등급을 숫자로 치환하고 이를 곱하여 total 변수에 합산한다.
# 20개의 과목 모두 합산되었다면 total 변수를 학점의 총합으로 나눠 평균을 구한다.
# 이를 출력한다. 각종 예외처리 사항은 이미 입력 측에 의해 처리된 상태이다.
# 조건대로 소수점 6번째 자리부터 반올림 처리한다

subjectCount = 20

totalScore = 0
totalCredit = 0
average = 0

for i in range(subjectCount):
    subject, credit, grade = input().split(' ')
    if grade != 'P':
        if grade == 'A+':
            totalScore += float(credit) * 4.5
        elif grade == 'A0':
            totalScore += float(credit) * 4.0
        elif grade == 'B+':
            totalScore += float(credit) * 3.5
        elif grade == 'B0':
            totalScore += float(credit) * 3.0
        elif grade == 'C+':
            totalScore += float(credit) * 2.5
        elif grade == 'C0':
            totalScore += float(credit) * 2.0
        elif grade == 'D+':
            totalScore += float(credit) * 1.5
        elif grade == 'D0':
            totalScore += float(credit) * 1.0
        elif grade == 'F':
            totalScore += float(credit) * 0.0
        totalCredit += float(credit)

print(round(totalScore/totalCredit, 6))
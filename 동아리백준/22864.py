# 1. 하루 한 시간 단위로 일을 하거나 쉴 수 있다.
# 2. 일을하면 A만큼 피로도가 증가하고 B만큼 작업이 처리된다.
# 3. 쉴 경우 C만큼 피로도가 감소한다.
# 4. 피로도가 M을 초과하면 일을 할 수 없다.
# 5. 피로도는 음수가 될 수 없다.
# 6. 하루는 24시간이다.
# 7. 하루에 M을 넘기지 않고 최대한 많은 작업을 할 수 있는지 출력한다.

# 한 시간 단위로 반복시키면 될 듯 하다.
# 조건문을 통해 추가 피로도 + 현재피로도 > M 이면 일을 휴식을 하고
# 그렇지 않으면 일을 하도록 한다. 또 휴식을 한 후 값이 음수면 0으로 변경하는 조건 또한 추가한다.
# 이를 24번 반복한다. 
import sys

input = lambda: sys.stdin.readline().rstrip()

A, B, C, M = map(int, input().split())
work = 0
stress = 0
for i in range(24):
    if stress + A <= M:
        work += B
        stress += A
    else:
        stress -= C
        if stress < 0:
            stress = 0

print(work)
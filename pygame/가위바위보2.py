"""
가위, 바위, 보 게임 만들기
-게임 방법
1. 당신(you)은 가위, 바위, 보 중 하나를 입력한다.
2. 컴퓨터(com)는 가위, 바위, 보 중 하나를 랜덤 생성한다.
3. 결과 출력은 무승부, 패, 승이다.
4. 잘못 입력한 경우 "잘못된 입력입니다. 다시 입력해 주세요"
"""

import random
import sys

print("♠가위 바위 보 게임을 시작합니다♠\n")
가위바위보 = ['가위', '바위', '보']

def play(you, com):


    if you not in 가위바위보:
        print("잘못된 입력입니다. 다시.")
        return

    if you == com:
        state = 0
    elif you == '가위' and com == '보':
        state = 2
    elif you == '바위' and com == '가위':
        state = 2
    elif you == '보' and com == '바위':
        state = 2
    else:
        state = 1

    print("결과 :", result[state])


result = {0: '무승부', 1: '패', 2: '승'}
state = 0 #상태 변수(0/1/2)

you = input('당신 : ')

com = random.choice(가위바위보)
print("컴퓨터 :", com)

play(you, com)
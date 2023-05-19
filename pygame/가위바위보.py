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

def fight():
    print("♠가위 바위 보 게임을 시작합니다♠\n")
    가위바위보 = ['가위', '바위', '보']
    you = input("'가위', '바위', '보' 중 하나를 정확하게 입력하세요 : ")
    if you not in 가위바위보:
        print("잘못된 입력입니다. 프로그램을 종료합니다.")
        sys.exit(0)  # 프로그램 즉시 종료

    print(f'당신 : {you}')
    com = random.choice(가위바위보)
    print(f'컴퓨터 : {com}')
    if you == com:
        print('결과 : 무승부')
    elif you == '가위' and com == '보':
        print('결과 : 승')
    elif you == '바위' and com == '가위':
        print('결과 : 승')
    elif you == '보' and com == '바위':
        print('결과 : 승')
    else:
        print('결과 : 패')

fight()

"""
※ 파이썬은 random.choice가 있어서 가능함 ※

# random.randint() 사용
rnd = random.randint(0, 2)
com = 가위바위보[rnd]
print("컴퓨터 :", com)
"""


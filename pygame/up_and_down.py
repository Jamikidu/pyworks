# 숫자 추측게임
"""
게임 방법
- 게임이 시작되면 컴퓨터가 난수(정답)를 생성한다.
- 사용자의 추측값이 정답과 같으면 '정답!',
  추측값이 정답보다 크면 "너무 커요!",
  추측값이 정답보다 작으면 '너무 작아요!' 출력
"""

import random

com = random.randint(1, 50)
print(com)
min_v = 1
max_v = 50

try:
    chance = 5
    while chance > 0:
        guess = int(input(f"예상되는 숫자를 입력하세요({min_v} ~ {max_v}) "))
        # 조건문 작성
        if guess < min_v or guess > max_v:
            print("범위가 넘어가버렸습니다. 다시 입력해주세요.")
        elif guess > com:
            print("너무 커요!")
            max_v = guess
            chance -= 1
            print("남은 기회 :", chance)
        elif guess < com:
            print("너무 작아요!")
            min_v = guess
            chance -= 1
            print("남은 기회 :", chance)
        elif guess == com:
            print(f"정답!! {com}")
            print(f"점수 : {chance * 10}점")
            break

    if (chance == 0):
        print("\tㅋㅋㅋㅋ 못 맞췄지롱~")
except ValueError:
    print("유효한 값이 아닙니다.")

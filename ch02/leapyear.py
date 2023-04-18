# 연습문제
# 2월 29일 - 윤년, 4년마다 오고, 100년 단위는 아니나
# 400년은 윤년이다.
# 조건1 - 4년마다 오고, 조건2 - 100년 단위는 아니나, 조건3 - 400년 단위는 윤년임
# 출력 - f string 방식(format)
# 예외(오류) 처리 - try 실행 except 처리구문
try:
    years = int(input("연도를 입력하세요 "))

    if (years % 4 == 0 and years % 100 != 0) or years % 400 == 0:
        # print(str(years) + "년은 윤년입니다")
        print(f'{years}년은 윤년입니다.')
    else:
        # print(str(years) + "년은 평년입니다")
        print(f'{years}년은 평년입니다.')
except ValueError:
    print("숫자를 입력해 주세요")
    

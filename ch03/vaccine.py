# 백신 접종자 분류
birth = input("출생년도를 입력하세요(yyyy) ")

age = 2023 - int(birth) + 1

if age >= 20 and age <=65:
    print("백신 접종 대상입니다")
    if birth[-1] == "1" or birth[-1] == "6":
        print("월요일 접종")
    elif birth[-1] == "2" or birth[-1] == "7":
        print("화요일 접종")
    elif birth[-1] == "3" or birth[-1] == "8":
        print("수요일 접종")
    elif birth[-1] == "4" or birth[-1] == "9":
        print("목요일 접종")
    elif birth[-1] == "5" or birth[-1] == "0":
        print("금요일 접종")
else:
    print("미 대상 - 하반기 일정 확인")

string = 'a:b:c:d'
string2 = string.split(':')
print(string2)
print(string2[-1])

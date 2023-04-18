# 조건문
# 삼항 연산자 - 조건 연산자 사용안함
# if문의 콜론(:) 코드 블럭을 의미하고
# 다음줄에서 4칸 들여쓰기(indent-인덴트) 되어야함
"""
result = (10 < -10) ? 'T' : 'F'
print(result)
"""

# 파이썬 if 문
"""
if 조건식:
    실행 1  # 4칸 들여쓰기(인덴트)
else:
    실행 2
"""

"""
x = 10
y = -10

if x < y :
    print("맞음")
else:
    print('틀림')
"""

# 자동차 주행 제한속도가 50km 이상이면 "안전속도 위반데쓰!! 과태료 10만원 부과대상"
"""
limit_speed = 60
if limit_speed >= 50:
    print("안전속도 위반데쓰!! 과태료 10만원 부과대상")
print("현재 속도는 " + str(limit_speed) + "km입니다.")
"""

# 자동차 주행 제한속도가 50km 이상이면 "안전속도 위반데쓰!! 과태료 10만원 부과대상"
# 50km 미만이면 "안전속도 시아준수"를 출력하는 프로그램

limit_speed = int(input("현재 차량 속도는? "))
if limit_speed >= 50:
    print("안전속도 위반데쓰!! 과태료 10만원 부과대상")
else:
    print("안전속도 시아준수")
print("현재 속도는 " + str(limit_speed) + "km입니다.")
    



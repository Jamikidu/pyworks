# 입력처리 - input()함수
# 방법1
"""
print("이름을 입력해 주세요")
name = input() # 문자를 입력할 수 있음
print(name + "님 사랑해요")
"""

# 방법2
# name = input("이름을 입력해 주세요")
# print(name)

# 입력받은 수는 문자열임 -> 정수로 변환이 필
"""
number = int(input("숫자를 입력해 주세요(1~10)"))
print(number * 2)
"""

# 두 수를 입력받아 합을 계산하기
"""
x = int(input("첫째 수 입력 :"))
y = int(input("둘째 수 입력 :"))
sum_v = x + y
print(sum_v)
"""

# 나이 계산 프로그램
# 현재년도 - 출생년도 + 1
"""
current_year = 2023
birthyear = int(input("태어난 년도는? "))

age = current_year - birthyear + 1
print("현재 나이는:", str(age) + "세")
"""

width = int(input("가로의 길이를 입력하세요 "))
height = int(input("세로의 길이를 입력하세요 "))

area = width * height
print("가로의 길이:", str(width) + "cm")
print("세로의 길이:", str(height) + "cm")
print("넓이:", str(area) + 'cm')
        

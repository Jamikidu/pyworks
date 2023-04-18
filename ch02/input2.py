# 입력 처리
"""
print("당신이 좋아하는 색깔은 무엇이에요?(흰색)")
color = input() # 키보드 입력 처리
print(color)
"""

# \n 은 줄바꿈, \t 는 탭
"""
color = input("당신이 좋아하는 색깔은 무엇이에요?(흰색)\t")
print("좋아하는 색깔은 " + color)
"""

# int() - 문자를 정수로 바꿔줌
number = int(input("숫자를 입력하세요 "))
print('입력된 수는 ', (number + 4), '입니다.')
print('입력된 수는 ', str(number + 4) + '입니다.')

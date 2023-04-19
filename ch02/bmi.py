# 체질량 지수 = 몸무게 / 키(m)의 제곱
# 거듭제곱 3 ** 2 = 3 x 3

print("☆★ BMI 지수 계산 프로그램 뿌슝빠슝 ★☆")
name = input("이름을 입력하세요 : ")
weight = float(input("몸무게(kg)를 입력하시오 "))
height = float(input("키(cm)를 입력하시오 "))
height = height / 100  # 키 cm를 미터(m)로 변환


bmi = weight / (height ** 2)

print(f'{name}님의 BMI는 {bmi:.2f}입니다.')   # f 스트링(string) 방식
print("%s님의 BMI는 %.2f입니다." % (name, bmi))   # % 포맷 방식

if bmi < 20:
    print('저체중 입니다.')
elif bmi >= 20 and bmi < 24:
    print('정상입니다.')
elif bmi >= 24 and bmi < 30:
    print('과체중입니다.')
else:
    print('돼지뇨속')

# random 모듈
# 숫자(정수)를 랜덤 추출 : random.randint(1, 10)
# 리스트에서 요소 추출 : random.choice(리스트)
import random

# 1 ~ 10 중 무작위로 추출
num = random.randint(1,10)
print(num)

# 주사위 만들기
dice = random.randint(1,6)
print(dice)

# 주사위 10번 던지기
for i in range(10): # 0~9(10번)
    dice = random.randint(1, 6)
    print(dice,end=' ')
    if i ==9:
        print(dice)


# 리스트에서 랜덤하게 값을 추출하기
과일 = ['딸기', '수박', '참외', '사과']
#print(과일[0])
#print(과일[-1])
print(random.choice(과일))

# 주사위 2개를 10번 던지기
# 두 눈의 합이 7이면 "Seven Thrown!!" 출력, 11이면 "Eleven Thrown" 출력
# 두 눈의 수가 같으면 ""Double Thrown!!!"
for i in range(10): # 0~9(10번)
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum_v = dice1 + dice2
    if sum_v == 7:
        print(f'두 주사위의 합: {sum_v} Seven Thrown!!')
    elif sum_v == 11:
        print(f'두 주사위의 합: {sum_v} Eleven Thrown!!')
    elif dice1 == dice2:
        print(f'두 주사위의 합: {sum_v} Double Thrown!!')
    else:
        print("두 주사위의 합: {}".format(sum_v))

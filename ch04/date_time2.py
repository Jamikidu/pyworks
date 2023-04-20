# 나이가 100세 되는 해의 연도 계산하기
# 현재년도 + (100-age)
import datetime
import calendar as car

# car.prcal(2023)  # 2023년 달력
car.prmonth(2021, 4)  # 2021년 4월 달력

now = datetime.date.today()
print(f'현재 년도는 : {now.year}')

age = int(input("나이 입력 : "))
result = now.year + 100 - age
print(f'당신이 100세가 되는 해 : {result}년')
# 지나온 날짜 계산하기 : 일수 = 종료일 - 시작일
# datetime.date(종료일) - datetime.date(시작일)
# 요일(인덱스) - datetime.date(특정일).weekday()
import calendar
import datetime

print(" ★☆ 지금까지 몇 일? ☆★")
day1 = datetime.date(2023, 3, 16)
print(day1)

today = datetime.date.today() # .today() 또는 date(2023, 4, 21)
print(today)

passed_time = today - day1
# print(passed_time)
# 날짜객체.days -> 일로 환산
print("개강 이후 {}일이 지났습니다".format(passed_time.days))

# 날짜로 요일 알아내기
days = ['월', '화', '수', '목', '금', '토', '일']

# datetime.date(2023, 3, 16).weekday()
the_day = datetime.date(2023, 3, 16).weekday()
print(days[the_day])  # the_day = 3
print(f'{days[the_day]}요일')
print("{}요일".format(days[the_day]))

now = datetime.date.today().weekday()
print(f'오늘은 {days[now]}요일')

# 2023. 3월 출력
calendar.prcal(2023)
calendar.prmonth(2023, 3)
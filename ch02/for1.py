# for ~ in range()
"""
for in in range(시작, 종료, 증감):

for i in range(1,11):
    print(i)
"""
# 1부터 10까지 출력
"""
for i in range(1, 11, 1):
    print(i, end=' ')
print()
print('=' * 15)
for i in range(10, 0, -1):
    print(i, end=' ')
print()
"""

# 1부터 10까지 합계
"""
sum_v = 0
for i in range(1, 11):
    sum_v += i
    print(f'i = {i}, sum_v = {sum_v}')
print(f'합계 : {sum_v}')
"""

# 1부터 10까지의 홀수 출력
"""
for i in range(1, 11):
    if i % 2 == 1:
        print(i, end=' ')
"""

num = [10, 50, 30, 70]

print(50 in num)
print(80 in num)
#리스트 출력
print(num)

# 전체 요소를 출력
for i in num:
    print(i)

# 50보다 큰 수를 출력하라
for i in num:
    if i > 50:
        print("50보다 큰 수:", i)

for i in ['Seoul', 'Incheon', 'Gwangju']:
    print(i[0], end='')
"""
 city[0] - 첫번째 i = Seoul  -> i[0] -'S'
 city[1] - 두번째 i = Incheon  -> i[0] -'I'
 city[2] - 세번째 i = Gwangju  -> i[0] -'G'
"""

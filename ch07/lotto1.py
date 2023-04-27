# 로또 복권 추첨 프로그램
import random

# 처리

lotto = []
while len(lotto) < 6:
    num = random.randint(1, 45)
    if num not in lotto:  # 중복 제거(5개만 저장되는 문제)
        lotto.append(num)

"""
for i in range(6):
    num = random.randint(1, 45)
    if num not in lotto:  # 중복 제거(5개만 저장되는 문제)
        lotto.append(num)
"""

# 출력
print(lotto)
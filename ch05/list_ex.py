# 리스트 복사
a = [1, 2, 3, 4, 5]
a2 = []

# a5 = for i in a if i % 2 == 0
# print(a5)
"""
for i in a:
    a2.append(3 * i)
"""
# 리스트 내포 - for문이 리스트 내부
a3 = [3* i for i in a]
print(a3)

a4 = []  # 3의 배수이면서 짝수인 수 저장
"""
for i in a:
    if i % 2 == 0:
        a4.append(3*i)
print(a4)
"""

a4 = [3 * i for i in a if i % 2 == 0]
print(a4)

# 1부터 10까지 저장하는 리스트
b = [i for i in range(1, 11)]
print(b)

b2 = [i for i in range(1, 11) if i % 2 == 0]
print(b2)
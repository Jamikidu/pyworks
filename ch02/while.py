# While 반복
# 'hello'를 10번 출력
"""
i = 0
while i < 10:
    i = i + 1
    print("Hello~", [i])
"""

# 1부터 10까지 더하기
"""
i = 0
sum_v = 0
while i < 10:
    i += 1
    sum_v = sum_v + i
    print("i =", i, "sum_v =", sum_v)

print(f'합계 : {sum_v}')
"""

# 반복 조건문(break)
"""
i = 0
sum_v = 0
while True:
    i += 1
     
    if i > 10:
        break
    sum_v += i
    print(f'i={i}, sum_v={sum_v}')
print(f'합계 : {sum_v}')
"""

while True:
    key = input("반복을 계속 할까요?(y/n)")
    if (key == "y" or key == "Y"):
        print("반복을 계속 합니다.")
    elif (key == "n" or key == "N"):
        print("반복을 중단합니다.")
        break
    else:
        print("정상 답변이 아닙니다.")
    

# 중첩 for문
"""
for i in range(5): #range(0, 5) -아무것도 안써있으면 생략된것
    print(i)
"""
# 5행 5열
for i in range(5):
    for j in range(5):
        print('$', end="")
    print()

# 스타(*) 출력
# 삼각형
for i in range(0, 5):
    for j in range(0, i+1):
        print('*', end="")
    print()
"""
i=0  j=0                      *
i=1  j=0, j=1                 **
i=2  j=0, j=2, j=3            ***
i=3  j=0, j=2, j=3, j=4       ****
i=4  j=0, j=2, j=3, j=4, j=5  *****
"""

# 1부터 증가하는 숫자 출력
for i in range(0, 5):
    for j in range(1, 6):
        print((5*i) + j, end=" ")  # 5는 j의 종료값
    print()
"""
1 2 3 4 5       -> (5*0)+1, (5*0)+2, (5*0)+3...
6 7 8 9 10      -> (5*1)+1, (5*1)+2, (5*1)+3...
11 12 13 14 15  -> (5*2)+1, (5*2)+2, (5*2)+3...
16 17 18 19 20
21 22 23 24 24

"""
row = 5
col = 5
for i in range(0, row):
    for j in range(1, col+1):
        num = (col*i) + j
        print(num , end=" ")  # 5는 j의 종료값
    print()

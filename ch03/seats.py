customer = int(input("입장객 수 입력: "))
col = int(input("좌석 열 수 입력: "))

# 몫 = customer // col
# 나머지 = customer % col
if customer % col == 0:
    row = customer // col
    #row = int(customer / col)
else:
    row = customer // col + 1
    #row = int(customer / col) + 1

# print("줄 수:", row)
# 좌석 배치
for i in range(0, row):
    for j in range(1, col+1):
        num = (col*i) + j
        if num > customer:
            break
        print(f'좌석{num}', end=" ")  # 5는 j의 종료값
        
    print()

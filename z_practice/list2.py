# 점수 리스트 선언 및 생성
score = [70 ,80, 50, 60, 90, 40]
sum_v = 0
for i in score:
    sum_v += i

count = len(score)
avg = sum_v / len(score)

print(f'리스트의 갯수 : {len(score)}')
print(f'리스트의 합계 : {sum_v}')
print(f'리스트의 평균 : {avg:.3f}')

# 내장함수 sum()과 비교

print(f'리스트의 합계 : {sum(score)}')
print(f'리스트의 평균 : {sum(score)/len(score):.4f}')

# 리스트의 최고점수
max_v = score[0]
for i in score:
    if max_v < i:
        max_v = i
print("최대값 : ",max_v)

# 최고 점수의 위치
max_idx = 0
n = len(score)
for i in range(1, n):
    if score[max_idx] < score[i]:
        max_idx = i

print("최고값 위치 : {}".format(max_idx))

# 리스트의 최저점수
min_v = score[0]
for i in score:
    if min_v > i:
        min_v = i
print("최소값 : ",min_v)

# 최저 점수의 위치
min_idx = 0
n = len(score)
for i in range(1,n):
    if score[min_idx] > score[i]:
        min_idx = i

print("최저값 위치 : ", min_idx)
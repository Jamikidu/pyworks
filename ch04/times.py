# 배수를 구하는 함수
# 배수의 개수를 구하시오


def times(x):
    global count
    for i in range(1,101):
        if i % x == 0:
            count += + 1
            print(i, end=" ")

count = 0
times(4)
print(f'\n배수의 개수 = {count}')
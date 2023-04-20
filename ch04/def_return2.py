# 사각형의 넓이 계산 함수
# 함수이름 - calc_area(), tri_area()

def calc_area(width,height):
    area = width * height
    return area

def tri_area(s,h):
    area = s * h / 2
    return area

# 가로 - 4cm, 세로 - 3cm
result = calc_area(4,3)
print('사각형의 면적', calc_area(4,3))  #12
print(f'사각형의 면적 {result}')

# 삼각형. 밑변 - 4, 높이 - 5
result2 = tri_area(4,5)
print("삼각형의 면적", tri_area(4,5))  #10
print(f'삼각형의 면적 {result2}')

# 정사각형의 면적
n = int(input("변의 길이를 입력: "))


def calc_size(n):
    area = n * n
    return area

print(calc_size(n))

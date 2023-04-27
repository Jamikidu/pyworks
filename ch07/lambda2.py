# map(), filter()
# 리스트를 매개변수로 전달
# lambda 함수와 map() 사용
# map()은 list()를 사용해서 리스트로 반환함
def times(x):
    return 3 * x

v = [1, 2, 3, 4]
#timess = lambda x : 3 * x
# map(함수, 리스트)
result = map(times, v)
#result = map((lambda x : 3* x), v)
print(list(result))


# filter()와 lambda 사용
# 음의 정수를 출력하시오
def negative(n):
    return n < 0

li = [-5, 1, 2, -11, 76]
#negative = lambda x : x < 0
value = filter(negative, li)  #filter(함수, 리스트)
print(list(value))
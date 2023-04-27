import time


start1 = time.time()
def getgob(n):
    gob = 1  # 곱셈에서는 1을 기억
    for i in range(1, n+1):
        gob = gob * i
    return gob

print(getgob(995))
end1 = time.time()
print(f'소요 시간1 : {end1-start1:.20f}')


start2 = time.time()
def facto(n):
    if n <= 1:
        return 1
    else:
        return n * facto(n-1)

print(facto(995))
end2 = time.time()
print(f'소요 시간2 : {end2-start2:.20f}')
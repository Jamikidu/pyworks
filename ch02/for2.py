# for ~ in
"""
languages = ['python', 'C', 'Java', 'Javascript']

for lang in languages:
             if lang in ['Python', 'Javascript']:
                 print(f'{lang} need interpreter')  #인터프리터
             else:
                 print(f'{lang} need complier') #컴파일러
"""
            
# 구구단 출력
dan = 4
result = ""

"""
for i in range(1, 10):
    print(f'{dan} x {i} = {dan * i}')
"""

"""
for i in range(1, 10):
    current_val = f'{dan} x {i} = {dan * i}\n'
    result = result + current_val;

print(result)
"""

coffee = 5

while True:
    try:
        money = int(input("돈을 넣어주세요: "))
        
        if money < 400:
            print("커피가 나오지 않습니다")
        elif money == 400:
            print("커피가 나옵니다")
            coffee -= 1  # coffee = coffee - 1
        elif money > 400:
            print(f'커피가 나오고, 거스름돈 {money-400}원을 돌려 받습니다')
            coffee -= 1
        print(f'남은 커피의 양은 {coffee}개 입니다.')
        # 커피가 0개이면  프로그램 종료

        if coffee == 0:
            print("커피가 모두 소진되었습니다. 판매를 중지합니다.")
            break
    except:
        #print("넌 먹을 자격이 없다. 나가라")
        pass    
        

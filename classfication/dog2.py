# Dog 클래스 - 정적 클래스
class Dog:
    #tricks = []  # 클래스 리스트

    def __init__(self,name):
        self.name = name
        self.tricks = []  # 인스턴스 리스트

    def add_trick(self, trick):
        self.tricks.append(trick)

dog1 = Dog("기쁨")
dog2 = Dog("사랑")

dog1.add_trick('몸 뒤집기')
print(dog1.name)
print(dog1.tricks)

dog2.add_trick('죽은척 하기')
print(dog2.name)
print(dog2.tricks)
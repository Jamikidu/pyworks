# 간단한 계산클래스 만들기
class Calculator:
    def __init__(self):
        self.x = 0

    def add(self, y):
        self.x += y
        return self.x

    def sub(self, y):
        self.x -= y
        return self.x


c1 = Calculator()
print(c1.add(10))
print(c1.sub(4))

c2 = Calculator()
print(c2.add(10.1))
print(c2.sub(2.5))
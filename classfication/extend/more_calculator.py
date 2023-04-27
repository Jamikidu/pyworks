from classfication.calculator2 import Calculator

# 거듭제곱 계산이 추가된 계산기
class MoreCalculator(Calculator):
    """
    # 파이썬만 있는 제곱 기능
    def pow(self):
        return self.x ** self.y
    """
    # 2의 4제곱 2x2x2x2
    def pow(self):
        num = 1
        for i in range(0, self.y):
            num = num * self.x
        return num


    def div(self):
        """
        if self.y == 0:
            return 0
        else:
            return self.x / self.y
        """

        try:
            return self.x / self.y
        except ZeroDivisionError as e:
            #return "0으로 나눌 수 없습니다."
            return e

cal1 = MoreCalculator(2, 4)
print(cal1.add())
print(cal1.sub())
print(cal1.mul())
print(cal1.div())
print(cal1.pow())

cal2 = MoreCalculator(4, 0)
print(cal2.div())
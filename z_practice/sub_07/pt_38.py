from z_practice.sub_07.pt_37 import Calculator


class MoreCalculator(Calculator):
    def pow(self):
        return self.x ** self. y

    def div(self):
        if self.y == 0:
            return 0
        else:
            return self.x / self.y


cal = MoreCalculator(2,4)
print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())
print(cal.pow(),"\n")

cal2 = MoreCalculator(5, 0)
print(cal2.add())
print(cal2.sub())
print(cal2.mul())
print(cal2.div())
print(cal2.pow())
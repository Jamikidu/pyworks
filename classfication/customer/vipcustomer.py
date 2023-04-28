# VIPCustomer 클래스 생성 - Customer 상속
# 멤버 변수 - 고객아이디, 이름, 고객등급, 구매할인율, 보너스 적립율
from classfication.customer.customer import Customer


class VIPCustomer(Customer):
    def __init__(self, cid, cname, agent):
        super().__init__(cid, cname)
        self.agent = agent
        self.cgrade = "VIP"
        self.sale_ratio = 0.1  # 10%
        self.bonus_ratio = 0.05  # 5%

    def __str__(self):
        return f'{super().__str__()}\n전문 상담원 ID는 {self.agent}입니다.'

    def calc_price(self, price):
        price -= int(price * self.sale_ratio)
        self.bonus_point += int(price * self.bonus_ratio)
        return price
if __name__=="__main__":
    vip1 = VIPCustomer(1004, "진", 777)
    price = 10000
    cost = vip1.calc_price(price)
    print(f'{vip1.cname}님의 구매비용은 {cost}원 입니다.')
    print(vip1)
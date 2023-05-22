# 건강 상태 클라스 만들기
# 운동을 하면 체력이 1 증가하고 술을 마시면 체력이 1 감소함
# 건강 상태 : hp로 설정, hp의 범위 : 1 ~ 100

class Health:
    def __init__(self, name):
        self.name = name
        self.hp = 10
        print(f'당신의 캐릭터명을 {self.name}으로 설정했습니다. 기본체력은 {self.hp}입니다.')

    def status(self):
        print("용사의 이름은", self.getname(), ",현재 체력은", self.gethp())

    def getname(self):
        return self.name

    def sethp(self, hp):
        if hp < 0:
            hp = 0
        if hp > 20:
            hp = 20
        self.hp = hp

    def gethp(self):
        return self.hp

    def 운동(self, hours):
        self.sethp(self.hp + hours)
        print("{0}시간 운동했습니다. 체력이 {0}만큼 증가합니다.".format(hours))
        print("현재 체력은 {}".format(self.hp))
        if(self.hp == 20):
            print("최대체력 20에 도달했습니다.더 이상 체력이 오르지 않습니다.")

    def 술(self, cups):
        self.sethp(self.hp - cups)
        print("술을 {0}잔 먹었습니다. 체력이 {0}만큼 감소합니다.".format(cups))
        print("현재 체력은 {}".format(self.hp))
        if (self.hp == 0):
            print("-----------------------------------------")
            print("Y  O  U  D  I  E")
            print("체력 0에 도달했습니다. 용사가 사망했습니다.")
            print("-----------------------------------------")


p1 = Health("홍길동")
p1.운동(5)
p1.status()
p1.술(3)
p1.운동(10)
p1.술(20)

p2 = Health("메이플도적")
p2.운동(3)
p2.술(5)
p2.status()





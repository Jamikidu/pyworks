# 건강 상태 클라스 만들기
# 운동을 하면 체력이 1 증가하고 술을 마시면 체력이 1 감소함
# 건강 상태 : hp로 설정, hp의 범위 : 1 ~ 100

class Health:
    def __init__(self, name):
        self.name = name
        self.hp = 10

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
        if(self.hp == 20):
            print("최대체력 20에 도달했습니다.더 이상 체력이 오르지 않습니다.")

    def 술(self, cups):
        self.sethp(self.hp - cups)
        print("술을 {0}잔 먹었습니다. 체력이 {0}만큼 감소합니다.".format(cups))
        if (self.hp == 0):
            print("체력 0에 도달했습니다. 용사가 사망했습니다.")


p1 = Health("홍길동")
print("용사의 이름은",p1.getname())
p1.운동(5)
p1.술(3)
p1.운동(10)
p1.술(20)
# print("용사의 현재 hp는",p1.gethp(),"입니다.")






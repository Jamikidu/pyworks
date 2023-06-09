# Airplane 클래스
# 클래스의 구성 요소 - 생성자 함수, 멤버변수, 멤버함수
class Airplane:
    # 기본생성자 - 인터프리터가 생성해 줌
    """
    def __init__(self):
        pass
    """
    def take_off(self):
        print("비행기가 이륙합니다.")

    def fly(self):
        print("비행기가 일반 비행중입니다.")

    def land(self):
        print("비행기가 착륙합니다.")


# 객체 생성 방법
if __name__=="__main__":
    air = Airplane()
    air.take_off()  # 메서드(함수) 호출
    air.fly()
    air.land()
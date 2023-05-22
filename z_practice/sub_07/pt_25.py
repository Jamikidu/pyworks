# 사번 자동 발급

class Employee:
    serial_num = 1000 # 기준값 (클래스 변수)

    def __init__(self,name):
        self.name = name
        Employee.serial_num += 1
        self.id = Employee.serial_num

        """ #인스턴스 변수인 경우
        self.serial_num = 1000
        self.serial_num += 1
        self.id = self.serial_num
        #이 경우는 무조건 1001로 나옴 
        """


    def __str__(self):
        return "사번 : {}, 이름 : {}".format(self.id, self.name)

e1 = Employee("가나다")
print(e1)

e2 = Employee("마바사")
print(e2)

e3 = Employee("아자차")
print(e3)

# 객체 리스트
employee = [
    Employee('구름'),
    Employee('별'),
    Employee('행성'),
    Employee('달')
]
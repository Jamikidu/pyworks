# super() 사용 - Employee의 멤버 있는 경우

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getname(self):
        return self.name

    def getage(self):
        return self.age


class Employee2(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def getid(self):
        return self.employee_id

e2 = Employee2("이강", 25, 101)
print("이름 : ", e2.getname())
print("나이 : ", e2.getage())
print("아이디 : ", e2.getid())
class Person:
    def __init__(self):
        self.name = ""
        self.age = 0

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

    def setage(self, age):
        self.age = age

    def getage(self):
        return self.age


p1 = Person()
p1.setname("흥부")
p1.setage(35)
print("이름 : ", p1.getname())
print("나이 : ", p1.getage())
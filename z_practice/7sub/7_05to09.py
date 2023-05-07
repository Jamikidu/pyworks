class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def learn(self):
        print(f'{self.name}가 수업을 듣습니다')

    def __str__(self):
        return "이름 : {}, 학년: {}".format(self.name, self.grade)


std1 = Student('김하나', 1)
#print(std1.name, std1.grade)
print(std1)

std2 = Student('박둘', 2)
#print(std2.name, std2.grade)
print(std2)
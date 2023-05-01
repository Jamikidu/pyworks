class Student:
    name = ""
    grade = 0

    def info(self):
        print(self.name, self.grade)

std1 = Student()
std1.name = '김하나'
std1.grade = 1
#print(std1.name, std1.grade)
std1.info()

std2 = Student()
std2.name = '박둘'
std2.grade = 2
#print(std2.name, std2.grade)
std2.info()
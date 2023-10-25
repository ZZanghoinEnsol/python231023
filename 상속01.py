# 부모 클래스
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

    def working(self):
        print("현재 작업중")

    def sleeping(self):
        print("현재 수면중")

#자식 클래스
class Student(Person):
    #초기화 메서드 덮어쓰기

    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self, name, phoneNumber)
        # self.name = name
        # self.phoneNumber = phoneNumber , 상속받고 init에 추가하여 반복정의 제거
        self.subject = subject
        self.studentID = studentID
    
    # 상속받은 메서드 덮어쓰기
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1}, 학과: {2}, 학번: {3})".format(self.name, self.phoneNumber, self.subject,self.studentID))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")

p.printInfo()
s.printInfo()
s.working()
s.sleeping()


# print(p.__dict__)
# print(s.__dict__)





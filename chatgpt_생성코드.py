class Person:
    def __init__(self, person_id, phone_number):
        self.id = person_id
        self.phone_number = phone_number

    def printInfo(self):
        print("ID:", self.id)
        print("Phone Number:", self.phone_number)

class Manager(Person):
    def __init__(self, person_id, phone_number, skill, title):
        super().__init__(person_id, phone_number)
        self.skill = skill
        self.title = title

    def printInfo(self):
        super().printInfo()
        print("Skill:", self.skill)
        print("Title:", self.title)

class Employee(Person):
    def __init__(self, person_id, phone_number, skill, title):
        super().__init__(person_id, phone_number)
        self.skill = skill
        self.title = title

    def printInfo(self):
        super().printInfo()
        print("Skill:", self.skill)
        print("Title:", self.title)

# Example usage
person = Person("1", "555-555-5555")
print("Person Information:")
person.printInfo()

manager = Manager("2", "555-555-5556", "Leadership", "Senior Manager")
print("\nManager Information:")
manager.printInfo()

employee = Employee("3", "555-555-5557", "Programming", "Software Developer")
print("\nEmployee Information:")
employee.printInfo()


# 주석추가 버젼

class Person:
    def __init__(self, person_id, phone_number):
        # Person 클래스의 생성자 메서드입니다.
        # person_id와 phone_number를 인스턴스 변수로 설정합니다.
        self.id = person_id  # ID 설정
        self.phone_number = phone_number  # 전화번호 설정

    def printInfo(self):
        # 인스턴스 정보를 출력하는 메서드입니다.
        print("ID:", self.id)  # ID 출력
        print("전화번호:", self.phone_number)  # 전화번호 출력

class Manager(Person):
    def __init__(self, person_id, phone_number, skill, title):
        # Manager 클래스의 생성자 메서드입니다.
        # Person 클래스의 생성자를 호출하고, skill과 title을 추가로 설정합니다.
        super().__init__(person_id, phone_number)  # Person의 생성자 호출
        self.skill = skill  # 스킬 설정
        self.title = title  # 직책(타이틀) 설정

    def printInfo(self):
        # 인스턴스 정보를 출력하는 메서드를 오버라이드하며, skill과 title도 출력합니다.
        super().printInfo()  # 부모 클래스의 printInfo 메서드 호출
        print("스킬:", self.skill)  # 스킬 출력
        print("직책:", self.title)  # 직책 출력

class Employee(Person):
    def __init__(self, person_id, phone_number, skill, title):
        # Employee 클래스의 생성자 메서드입니다.
        # Person 클래스의 생성자를 호출하고, skill과 title을 추가로 설정합니다.
        super().__init__(person_id, phone_number)  # Person의 생성자 호출
        self.skill = skill  # 스킬 설정
        self.title = title  # 직책(타이틀) 설정

    def printInfo(self):
        # 인스턴스 정보를 출력하는 메서드를 오버라이드하며, skill과 title도 출력합니다.
        super().printInfo()  # 부모 클래스의 printInfo 메서드 호출
        print("스킬:", self.skill)  # 스킬 출력
        print("직책:", self.title)  # 직책 출력

# 예제 사용
person = Person("1", "555-555-5555")
print("Person 정보:")
person.printInfo()

manager = Manager("2", "555-555-5556", "리더십", "고급 매니저")
print("\n매니저 정보:")
manager.printInfo()

employee = Employee("3", "555-555-5557", "프로그래밍", "소프트웨어 개발자")
print("\n직원 정보:")
employee.printInfo()

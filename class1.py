# 객체중심 프로그램(Object Oriented Programming , OOP)
# 함수가 수백개가 되면, 관리를 어떻게 진행할 것인가 ? 

# 클래스가 쿠키의 틀이라면, 인스턴스(객체)는 그 쿠키틀로 찍어낸 반죽이다. 실제 함수(=메서드)는 해당 인스턴스를 토대로 진행이 될 것이다. 
# 주요한 라이브러리들은 클래스 기반으로 진행이 되니까, 이것을 배운다고 생각할 것. 


# 클래스 정의
class Person :
    #초기화 메서드
    def __init__(self):
        self.name = "default name"
    
    def print(self):
        print("My name is {0}".format(self.name))

    def name_change(self):
        name = input("신규 지정할 이름을 입력하세요. : ")
        self.name = name
    
# 인스턴스 생성
p1 = Person()
p2 = Person()
p1.print()

p1.name_change()
p1.print()

# 런타임 시 변수 추가
Person.title = "new title"

print(p1.title)
print(p2.title)
print(Person.title)

# 


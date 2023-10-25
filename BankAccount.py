# BankAccount.py

# 클래스 내에서는 해당 기능들이 정상적으로 작동할 수 있으나
# 클래스 밖에서는 해당 인스턴스 내 변수로 직접적으로 접근하지 못하도록 하는게 맹글링 이다. 

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    # 인스턴스의 문자열. 해당 인스턴스를 내가 문자열로서 정의해버리는 것임. print(객체.메소드1, 메소드2.. 하기는 귀찮으니까)
    def __str__(self):
        return "{0} , {1} , {2}".format(self.id, \
            self.name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)

account1.withdraw(3000)

#account1.__balance=150000000

print(account1)

# 읽기
# print(account1.__balance)

# 클래스 상속
# 부모클래스(=super class) / 자식클래스(=sub class)



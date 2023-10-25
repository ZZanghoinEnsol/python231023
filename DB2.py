# Database(DB or RDB)

# 데이터베이스와 파이썬의 관계는, 파이썬이 데이터를 끌어올리는 느낌. 파이썬에서 작성된 쿼리를 DB로 떨구고, 해당하는 데이터를 파이썬으로 그대로 올림.
# 만약 DB 관련 경험이 없다면 , 오픈소스인 SQLite 공부해보는 것도 나쁘지 않다. 

#SQL 관련 언어설명
# - DDL (data definition language) : 데이터베이스의 객체를 생성,수정,삭제하는 언어 → Create, alter, drop .. 
# - DML (data manipulation language) : 데이터를 다루는 언어 → select update insert delete ... (=.CRUD)

# 목적은 파이썬에서 DB를 체계적으로 관리하는 것이므로, 파이썬에서 관련 SQL구문을 쓰고 / DB 를 다뤄보는 것이다. 실제 DB SW에 연동해서 하는 것

# sqlite 모듈 : DB 등 전역함수가 정의되어 있음. 
# 전역함수 : sqlite3.connect / sqlite3.complete_statement / sqlite3.register_adapter / sqlite3.register_converter....
# connection 클래스 : cursor / rollback / commit / close / execute...

# ? Java JDBC / ODBC → 1. connection class(연결 맺고끊는 작업) 2. Command class(실제 SQL 실행) 3. ResultSet class(결과 집합)
# ? C#/VB : 1. connection class(연결 맺고끊는 작업) 2. command class(실제 SQL 실행) 3. Dataset Class(결과 집합)
# ? Python : 1. Connection class(연결 맺고 끊는 작업) 2. Cursor Class (command + result class 통합의 역할) → 두 클래스만 배우면되니 훨씬 Simple 함.

import sqlite3 

# 연결객체
#con = sqlite3.connect(":memory:") 구조 문제가 없다면, 가상 메모리 상 데이터구조가 아닌 실제 파일로서 진행하므로, 아래의 문장을 쓰는게 맞다. 
con = sqlite3.connect("c:\\work\\sample.db")

#커서객체 생성
cur = con.cursor()
#테이블 구조 생성
cur.execute("""create table if not exists PhoneBook
(id integer primary key autoincrement, name text, phoneNum text);
""")

#1건 입력
cur.execute("insert into PhoneBook (name,phoneNum) values ('전우치','010-222');")

# 입력 파라메터 처리
name = "홍길동"
phoneNumber = "010-333"
cur.execute("insert into PhoneBook (name,phoneNum) values (?,?);",(name,phoneNumber))
# ? 는 향후 치환될 변수를 나타냄. 여러개를 한번에 묶어서 치환할거니, Tuple로 처리를 하였음. 

# 다중 행입력
datalist = (("박문수","010-333"),("김길동","010-567")) # 2차원 행렬데이터. 튜플 / 튜플이 되어도 되고 , 튜플 / 리스트의 구조가 되어도 된다. 
cur.executemany("insert into PhoneBook (name,PhoneNum) values (?,?);",datalist) # datalist 내부에 여러개의 데이터가 존재를 하니.. 존재하는 데이터들을 업데이트 할 필요가 있다. 

#검색
cur.execute("select * from PhoneBook;")
for row in cur :
    print(row)



# 현재 데이터들은 모두 메모리에 저장이 되어있으며, fetchone() 혹은 fetchmany(), fetchall()을 쓰게되면 해당메모리에 있는 값 띄우면서 없애버린다.
# 그 메모리들은 Cursor 기반으로 생성이 되기 때무에, fetch를 쓰더라도 Cursor 로 select 구문 재실행해준다면 메모리에 다시 등록이 되므로 상관이 없다. 
# fetch 다 털고나서 상단의 for row in cur : print(row) 쓰면 안나오는 부분을 잘 보면 될 것이다. 
print("---fetchall()---")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())

# for row in cur :
#     print(row)

# 어지간한 DB 언어들은 Commit 처리를 안하면 롤백 되는 것이 기본이다. IDLE 에서 직접 확인 진행했음. 
# 작업완료 (Commit)

con.commit()











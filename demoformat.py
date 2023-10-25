# 표현1. print("{0:x}".format(a)) → format 내의 문자를 {} 내의 0에 대입을 하는데. {X}내의 포맷으로 처리한다. , b x 등으로 정리 가능하다.
# 표현2. print("x*x = ",str(x*x).rjust(3)) → 우측정렬로 3자리 까지만 정리 등. 전체 서식에 대한 방식정의 가능 

for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("-------오른쪽 정렬------")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).rjust(3))

print("-------0출력------")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).zfill(5))

# url1 = "http://www.multicampus.com/?page=" +1
# print(url1)    

url2 = "http://multicampus.com/?page=" + str(5)
print(url2)

for i in range(1,11):
    url3 = "http://multicampus.com/?page=" + str(i)
    print(url3)

print("----서식지정----")
print("{0:x}".format(10)) # hex
print("{0:b}".format(10)) # binary
print("{0:,}".format(15000))
print("{0:e}".format(4/3)) # exponential
print("{0:f}".format(4/3)) # fixed format
print("{0:.2f}".format(4/3)) # 소수점 이하 2자리까지

print("----파일 입출력----")

# 파일쓰기
f = open("demo.txt","wt",encoding="utf=-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

# 기존 파일에 첨부
f = open("demo.txt","a+", encoding="utf-8") # append 는 파일의 끝부분을 찾아서 알아서 감. 
f.write("다른 내용을 첨부\n")
f.close()

# 파일읽기
f = open("demo.txt","rt",encoding="utf=-8")
result=f.read()
print(result)


# read 함수 : 기본적으로 모든 문자를 str로 받아오는데, 파일이 너무 길 경우 readlines()를 써서 list형으로 받아오는게 좋다. 
# readlines() 를 쓴다고 할 때, 어디까지 읽어올 것인가? → EOF (End of File) 까지 while 반복구문을 진행함. 

# File pointer : 책갈피의 역할. seek()[원하는 위치로 파일포인터 이동] 와 tell()[현재 어디까지 읽었는지 반환함.] 을 많이 쓴다. 

# 처음으로 리셋

f.seek(0)
print(f.readline(), end="") # print 함수 끝에 \n 이 있는데, 숨겨져있음. 그걸 없애주는 역할.
print(f.readline(), end="") # print 함수 끝에 \n 이 있는데, 숨겨져있음. 그걸 없애주는 역할.


print("readlist 함수")

f.seek(0)
lst = f.readlines()
for item in lst : 
    print(item, end="")
f.close()



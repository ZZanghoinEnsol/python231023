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

# 파일읽기
f = open("demo.txt","rt",encoding="utf=-8")
result=f.read()
print(result)
f.close()


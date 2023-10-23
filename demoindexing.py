# Demoindexing.py

x = 100
y = 3.14

print(type(x))
print(type(y))

strA = "Python is very powerful"
strB = "파이썬은 강력해"

print(len(strA))
print(len(strB))

lst = [1,2,3]

# 디버깅 시, 중단점 기능(Break point)
# F5 를 통해 디버깅하면서 줄단위 실행을 할 수 가 있고, 이후 상단툴바에서 줄 단위 실행을 할 수 있게 됨. 
for item in lst:
    print(item)


#strA = "Python is very powerful"
#strB = "파이썬은 강력해"

# : 뒤에 있는 것은 리미트라, 그 앞에서 끊기도록 설계되어있음. : 뒤에 아무것도 없다면 끝까지를 나타냄.
print(strA[0])
print(strA[1])
print(strA[0:5])
print(strA[:6])

strC = """이 문자열은
다중라인으로
저장합니다.
"""
print(strC)
print("이 문자열은\\t를 입력할 시 무엇이 출력되는지를 보여주는 문자열이고, \t 를 출력합니다.")

colors = ["red","blue","green","purple"]
print(type(colors))
print(colors)

# 리스트 내 추가하는 방법은 append 혹은 insert 를 통해 작업할 수 있다. 
colors.append("yellow")
colors.insert(3,'black')
print(colors.index("black"))
print(colors)

colors.count("red")

# pop 기능 : 보여준 후 삭제하는 기능
# remove기능 : 보여주지 않고 단순히 삭제. 
# 정렬기능 : Sorting ( 오름차순 ) / reverse( 내림차순 )

# VB에서 명령어 추가할 때 는 3개정도 쓰고 탭 키, IDLEㅇ ㅔ서는 CTRL + space




# func3. 

# 들여쓰기
# -. 가장 바깥쪽 블록 코드는 반드시 1열부터 시작해야한다
# -. 내부 블록은 같은 거리만큼 들여써야하며, 블록 끝은 들여쓰기가 끝나는 부분으로 가주된다. 탭과 공백은 섞어쓰지 말고, 공백을 쓰고자 한다면 2~4칸 통일.
# -. 함수 / 분기 및 반복문 / 클래스 정의에서 사용한다. 


# for / if 중 continue / break 존재. break 면 루프파괴, continue는 루프 계속진행
# range : 수열생성 /
# ex. range(10) : 0,1,2,...10
# ex. range(5,10) : 5,6,7...10
# ex. range(10,20,2) : 10,12,14,..20


# 필터링 함수
lst = [10,25,30]
iterL = filter(None,lst)
# filter 는 자체 내장함수인데, 입력받는 리스트에서 조건을 걸어서 걸러냄. 지금은 별도로 조건 안걸어두니까 None 처리함.
for item in iterL:
    print(item)

print("---필터링 하는 경우")

def getBiggerThan20(i):
    return i>20

iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

#만약 이런 케이스(위에서 간단한 함수 만들고 이후 함수 적용하는 꼴)에 람다함수를 적용한다면, 좀 더 편하게 처리할 수 있음. 

print("---람다함수 적용")

iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print("람다함수 적용된 값:",item)
    print("람다함수 적용된 값: {0} ".format(item))

# 통 주석처리 및 제거 : ctrl + /


# #분기 구문
# score = int(input("점수 입력:"))
# if 90 <=score <= 100:
#     grade = "A"
# elif 80 <=score <=90:
#     grade= "B"
# elif 70 <=score <=80:
#     grade= "C"
# else:
#     grade= "D"

# print("등급은, {0} 입니다.".format(grade))    

# 반복구문

value = 5
while value >0:
    print(value)
    value -= 1

lst = ["Apple",100,3.15]
for item in lst:
    print(lst, type(lst))

fruit = {"apple":100, "kiwi":200}
for item in fruit.items():
    print(item)


fruit = {"apple":100, "kiwi":200}
for item in fruit.keys():
    print(item)

fruit = {"apple":100, "kiwi":200}
for item in fruit.values():
    print(item)


# break 구문
lst = list(range(1,11))
print(lst)

for i in lst:
    if i>5:
        break
    print("item:{0}".format(i))

# continue 함수

lst = list(range(1,11))
print(lst)

for i in lst:
    if i%2 ==0: # 만약에 짝수라면.. 
        continue # 이번 루프는 여기서 끝내고, 다음 스텝으로 이어가 ~ 
    print("item:{0}".format(i))

# 수열함수 range
print(list(range(2000,2024)))
print(list(range(1,32)))


# for 구문이 파이썬에서 없는 대신, for in 루프를 생성해서 유사코드를 작성할 수 있다.

for i in range(5+1):
    print(i)





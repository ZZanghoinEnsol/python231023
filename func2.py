# Lecture 5. 키워드 인자 및 스코핑룰
# 스코핑 룰 : 일반적으로 함수에서 입력받는 변수의 우선순위는 지역변수→전역변수 이다. 지역변수 내에서 해결이 안되는 경우 전역변수 검색하여 들고오는 꼴이다. 
# 키워드인자 : 입력파라미터가 너무 많아지게 되면, 순서에 맞춰서 넣는다손치면 순서틀리면서 이상하게 들어갈 수 있으니까 인자명을 앞에 붙여주는 방식.
# 가변인자 : 특정 함수에 포함될 파라미터가 정해지지 않아서, 개수 지정을 할 수 없을 때  인자를 Tuple 로 뽑아버리는 것임.

# 스코핑 룰
x = 1
def func1(a) : 
    return a+x

#호출 
print(func1(1))

def func2(a):
    x=5
    return a+x

#호출
print(func2(1))

# 기본값이 있는 경우
def times(a=10,b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

#키워드 인자방식
def connectURI(server,port):
    strURL = "http://" + server + ":" + port
    return strURL

#호출
print(connectURI("multi.com","80"))
print(connectURI(port="8080", server="multi.com"))

#가변인자 : 가변적상황

def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

# 호출
print(union("HAM","SPAM"))
print(union("HAM","SPAM","EGG"))


# 람다함수 : 파이썬에서는 이름이 없고, 함수 객체만 존재하는 익명함수. 이름이 함수식만 간결하게 작성해버림. 
# 람다함수를 쓰는 경우는 함수의 입력파라미터 혹은 리턴값으로 함수를 정의할 때 쓰는 중임. 일회성으로 써버리기 때문에, 변수나 결과에 대한 로그가 안남아있음. 

g = lambda x,y:x*y
print(g(3,4))

print((lambda x:x*x)(3))




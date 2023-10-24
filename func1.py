# 함수정의

def setvalue(newvalue):
    x = newvalue
    print(x)

setvalue(5)

# 값을 리턴하는 함수
def swap(x,y):
    return y,x

# 함수호출
result = swap(5,6)
print(result)

# 함수 밖에서 쓸 수 있게되면 전역변수, 
# 함수 안에서 끝나고 증발하는 변수들은 지역변수


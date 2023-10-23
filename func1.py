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
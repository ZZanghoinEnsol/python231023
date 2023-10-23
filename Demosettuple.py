# Demosettuple

# 튜플이 리스트 대비 갖는 장점은 속도이다. 읽기전용이기 때문에 굉장히 빠르다. 
# 변수 앞에 붙이는 *는 tuple, **는 set를 명기해주는 역할이다. 별다른 역할은 없음. 

#set는 중복을 자동으로 제거하여 세트를 생성하도록 되어있다.
a = {1,2,3,3}
b = {3,4,5,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# print(a[0]) set나 dictionary는 순서가 없으므로, index가 들어간 명령어가 작동이 되질 않음.

print("----Tuple 형식 ----")
tp = (1,2,3)
print(tp)
print(len(tp))
print(tp[0])

print("id: %s, name:%s" %("kim","김유신"))

# 함수정의

def calc(a,b):
    return a+b,a*b

# 함수호출
print(type([calc(3,4)]))

#★★★ 맨날 나오는 함수 : list int str range ★★★#





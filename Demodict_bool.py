# Demodict

phone = {"kim":"1111","lee":"2222","park":"3333"}

print(phone)
print(phone.keys())
print(len(phone))
print(phone["kim"])
print("park" in phone)
print("kang" not in phone)


print(phone.values())


#파이썬은 값형식과 참조형식 중 참조형식을 따른다른 증명
# p를 phone 에 대해 신규로 파줬다고 생각했지만, p에서 바꿔도 phone에서도 적용이 되어 나타난다. 

p = phone
print(p)
print(phone)

p["song"] = "1234"

print(p)
print(phone)


# 장비관리
# 초기 데이터형식 지정은 {}로 지정을 해서 key 값을 앞에 묶어주면 되는건데,
# 향후에 해당 Column 에 대한 지정은 []로 key를 묶어줄 수 있다. 

device = {"아이폰":5 , "아이패드":10}
print(device["아이폰"])

device["맥북"] = 15
device["아이폰"] = 6
print(device)

del device["아이폰"]
print(device)


## Python 주요 Boolean
# True / False / None(=null or NULL or NaN) 의 경우, 첫 문자는 대문자로 진행을 한다. 
# bool : 숫자가 0 이거나, 문자가 비어있거나다면 False. 나머지의 경우 True

# 다른 곳에서는 전부 Null 로 작성을 하지만, 파이썬에서는 None 으로 처리를 함. 
# 널널한 개발자 유튜브 ~~

isRight = False
print(type(isRight))

# And 와 Or 는 True 의 존재여부를 확인하는 것이다. 

for item in device.items():
    print(item)

for item in device.keys():
    print(item)

for item in device.values():
    print(item)


print(bool(0))
print(bool(3))
print(bool(""))
print(bool("test"))
print(bool([]))
print(bool([1,2,3]))
print(1<2)
print(1 !=2)
print(1==2)
print(True and True and True)
print(True and False and True)
print(False or True)


print(7/3) # 실제 나눗셈 값
print(7//3) # 정수 몫만 Return
print(7%3) # 나머지만 Return

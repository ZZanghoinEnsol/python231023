# Demostr.py

strA = "파이썬은 강력해"
strB = "python is very powerful"

print(len(strA))
print(len(strB))
print(strB.capitalize())
print(strB.count("p"))
print(strB.count("p",0,7))
print(strB.startswith("python"))
print(strB.endswith("ful"))

print("====MBC 확인====")
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

print("====Split and join====")
data = "<<< spam and ham >>>"
# result = data.strip() # 리스트 앞 / 뒤 공백 제거
result = data.strip("<> ") # 리스트 앞 <,>, 공백이 있다면 해당 항목을 제거함. 제거 글자를 지정가능한 장점이 있음. 

print(data)
print(result)

result2= result.replace("spam","spam egg")
print(result2)

result2 = "spam::egg::ham"
print(result2)
lst = result2.split(":") # split 은 공백일 시 공백문자를 기준으로 리스트화하여 찢어줌. 문자를 지정하여주면, 해당 문자를 빼면서 벽을 하나넣는다고 생각하면 됨 .
# lst = result2.split("::")

print("리스트:",lst)
print("====다시 합치기 ====")
print(":)".join(lst))


# DemoRE.py

# 정규표현식(re)
# -. 특정한 규칙을 나타내는 포맷 같은 느낌의 자체 표현식. 이메일 / 주민번호 / 연도 / 숫자연속 4자리.. 등 특정 패턴을 보는 것. 
# -. 웹 크롤링 등을 할 때, 내가 보고싶은 포맷의 데이터만 끌고오기 위한 것. 
# -. 파이썬 내부에 존재하는 간이언어(정규표현식 전용문법)를 쓰는 것이며, 타 언어에서도 거의 유사함. 

import re

result = re.search("[0-9]*th","35th")
print(result) # 매칭결과가 길게 나타남. 명확하지 않음.
print(result.group()) # 함수실행결과, 찾은 문자열만 뽑아냄. 

result = re.match("[0-9]*th","35th")
print(result)
print(result.group()) # 함수실행결과, 찾은 문자열만 뽑아냄. 

# 빈칸추가
# print("빈칸 추가")
# result = re.search("[0-9]*th"," 35th")
# print(result)
# print(result.group())

# result = re.match("[0-9]*th"," 35th")
# print(result)
# print(result.group())

print("결과2")

result = re.search("apple","this is apple")
print(result.group())

result = re.search("\d{4}","올해는 2023년 입니다.")
print(result.group())

result = re.search("\d{5}","우리동네는 52300 이다.")
print(result.group())

print("---- 대소문자 변환 ----")
result = re.search("apple","this is Apple".lower())
print(result.group())

# 컴파일 함수 사용
print("---- 컴파일 함수 사용 ----")

data = "Apple is big company and apple is delicious"
c = re.compile("apple",re.IGNORECASE) # 미리 컴파일을 해서, 찾기위한 포맷을 미리 걸어두는 것. 옵션은 ignorecase 처럼 줄 수 있는데, ignorecase는 대소문자 구분 없음.
print(c.findall(data)) # 컴파일 된 포맷을 전체 데이터 중에서 실행.

data = """다중 라인으로
만든 문자열

데이터"""
c = re.compile("^.+",re.MULTILINE)  # 마찬가지로 가능하나, ^.+는 시작하는 문자가 하나 이상이라는 뜻, 즉 공란을 제거한다는 의미이다. 
                                    # 단, 해당 데이터에 대해서는 여러 줄 일 수 있으니.. 여러 라인을 다 보라는 옵션이다. (re.MULTILINE)
print(c.findall(data))



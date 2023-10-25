# DemoOS.py

# from os.path import *
# abspath('tmp') : 현재 경로를 prefix로 하여, 입력받은 경로를 절대 경로로 반환한다.
# basename(path) : 입력받은 경로의 기본이름을 반환한다.(상세경로 다 빼고 파일이ㅡㅁ만)
# exists(path) : 입력된 경로가 존재하는 경로라면 True
# isfile(),isdir() : 입력받은 경로 혹은 파일이 실제로 파일인지 / 경로인지 확인.
# getctime() : 입력받은 경로(=파일)에 대한 생성시간을 반환한다. * Create Time
# getsize(path) : 파일의 바이트 단위 파일크기
# join(path1,path2,...) : 입력받은 경로를 연결함.
# normpath(path) : OS에 맞게 입력받은 경로 문자열을 정규화한다. 

# OS모듈 : 운영체제에서 제공하는 정보를 검색하거나, 외부실행파일을 실행할경우 사용되는 함수 제공 .
# glob 모듈 : 윈도우 dir 명령이나 리눅스의 ls 명령어와 유사기능. glob.glob(path) : 경로에 대응되는 모든 파일 및 디렉토리 리스트 반환
# glob.iglob(path) : glob과 동일하며, 주로 glob을 쓰긴함.

from os.path import *
from os import *
import glob

# 
print("전체경로:",abspath("python.exe"))
print("파일명: ",basename("c:\\work\\demo.txt"))

# 특수문자 가공하지 않은 상태(raw string notation). \를 두개씩 쓰기 싫을 때 사용가능한 코드. 
strPython = r"c:\python310\python.exe"
#strPython = "c:\\python310\\python.exe"
if exists(strPython):
    print("파일크기 : {0} Bytes".format(getsize(strPython)))
else :
    print("파일없음")

#외부 실행파일
#system("notepad.exe")

#운영체제
print("운영체제 이름 : ",name) 
print("환경변수: ",environ)

# result = glob.glob("c:\\work\\*.py")
# print(result)

for item in glob.glob("c:\\work\\*.*"):
    print(item)
    


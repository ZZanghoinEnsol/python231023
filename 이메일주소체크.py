import re

# 수정된 정규 표현식 패턴
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}.*$'
"""
^ - 문자열의 시작을 나타냅니다.
[a-zA-Z0-9._%+-]+ - 이메일 주소의 로컬 부분을 나타냅니다. 영문 대소문자, 숫자, 그리고 일부 특수 문자를 포함합니다.
@ - 이메일 주소에서 "@" 기호를 나타냅니다.
[a-zA-Z0-9.-]+ - 이메일 주소의 도메인 이름 부분을 나타냅니다. 영문 대소문자, 숫자, 그리고 일부 특수 문자를 포함합니다.
\.[a-zA-Z]{2,} - 이메일 주소의 최상위 도메인을 나타냅니다. 적어도 2개 이상의 영문 대소문자로 이루어져야 합니다.
.*$ - 문자열의 나머지 부분을 나타냅니다.
$ - 문자열의 끝을 나타냅니다.
"""

# 샘플 이메일 주소
emails = [
    "john.doe@example.com",   # 유효한 이메일 주소
    "jane_doe123@gmail.com",  # 유효한 이메일 주소
    "user@sub.domain.co.uk",  # 유효한 이메일 주소
    "invalid_email.com",      # 유효하지 않은 이메일 주소 (맨 뒤에 .이 누락됨)
    "name@.com",              # 유효하지 않은 이메일 주소 (도메인 부분이 누락됨)
    "alice.smith@company.org",       # 유효한 이메일 주소
    "1234@example.net",              # 유효한 이메일 주소
    "test_user@my-website.io",       # 유효한 이메일 주소
    "user12345@email.co",            # 유효한 이메일 주소
    "james@email-domain.co.uk",      # 유효한 이메일 주소
    "test.email@subdomain.company.org",  # 유효한 이메일 주소
    "user@valid-domain.io",            # 유효한 이메일 주소
    "email@website.info",             # 유효한 이메일 주소
    "example123@domain.co",           # 유효한 이메일 주소
    "name@personal.email"             # 유효한 이메일 주소
]

# 이메일 주소가 유효한지 확인
for email in emails:
    if re.search(email_pattern, email):
        print(f"{email}는 유효한 이메일 주소입니다.")
    else:
        print(f"{email}는 유효하지 않은 이메일 주소입니다.")

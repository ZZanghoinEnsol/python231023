import re

def is_valid_korean_rrn(rrn):
    # 정규 표현식 패턴: 6자리 연도(YYMMDD) - 7자리 (1: 남자, 2: 여자)
    pattern = r"^\d{6}-[12]\d{6}$"
    
    if re.match(pattern, rrn):
        birth_date = rrn[:6]  # 주민등록번호에서 생년월일 부분 추출
        gender = rrn[7]  # 성별 부분 추출

        # 생년월일 유효성 검사
        year = int(birth_date[:2])
        month = int(birth_date[2:4])
        day = int(birth_date[4:6])
        if not (1800 <= year <= 2099 and 1 <= month <= 12 and 1 <= day <= 31):
            return False

        # 성별 유효성 검사
        if gender not in ('1', '2'):
            return False

        return True
    else:
        return False

# 10개의 샘플 주민등록번호를 테스트
sample_rrns = [
    "950101-1234567",  # 유효한 남성 주민등록번호
    "030304-2345678",  # 유효한 여성 주민등록번호
    "980101-1234567",  # 유효한 남성 주민등록번호
    "050601-3456789",  # 유효한 여성 주민등록번호
    "881212-1234567",  # 유효한 남성 주민등록번호
    "040630-2345678",  # 유효한 여성 주민등록번호
    "731231-1234567",  # 유효한 남성 주민등록번호
    "081231-2345678",  # 유효한 여성 주민등록번호
    "991299-1234567",  # 유효한 남성 주민등록번호
    "020229-2345678",  # 유효한 여성 주민등록번호
]

for rrn in sample_rrns:
    if is_valid_korean_rrn(rrn):
        print(f"{rrn}은(는) 유효한 한국 주민등록번호입니다.")
    else:
        print(f"{rrn}은(는) 유효하지 않은 한국 주민등록번호입니다.")

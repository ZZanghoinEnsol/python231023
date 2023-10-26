import requests
from bs4 import BeautifulSoup
import openpyxl

# 결과를 저장할 Excel 파일 생성
workbook = openpyxl.Workbook()
worksheet = workbook.active

# 엑셀 파일 헤더 추가
worksheet.append(["블로그 명", "블로그 주소", "글의 주소", "작성일자"])

# 1페이지부터 100페이지까지 순회
for page in range(1, 101):
    # 각 페이지에 대한 URL 생성
    url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EB%A7%A5%EB%B6%81&start={(page - 1) * 10 + 1}"

    # URL로 HTTP GET 요청 보내기
    response = requests.get(url)

    # 요청이 성공했는지 확인
    if response.status_code == 200:
        # 페이지의 HTML 내용 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 블로그 글 정보가 포함된 요소 찾기
        post_items = soup.find_all('li', class_='bx')

        # 블로그 글 정보를 추출하고 엑셀 파일에 추가
        for post_item in post_items:
            blog_name = post_item.find('a', {'class': 'title_link_cross_trigger'})
            if blog_name:
                blog_name = blog_name.text
            else:
                blog_name = "N/A"

            # blog_address = post_item.find('a', {'class': 'nickname'})['href']
            #post_address = post_item.find('a', {'class': 'sh_blog_title'})['href']

            # creation_date = post_item.find('dd', class_='sub').text

            # 정보를 엑셀 파일에 추가
            worksheet.append([blog_name])
    else:
        print(f"페이지 {page}를 가져오지 못했습니다. 상태 코드:", response.status_code)

# 결과를 Excel 파일로 저장
workbook.save("C:\\work\\result.xlsx")

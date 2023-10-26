import requests
from bs4 import BeautifulSoup

# 크롤링할 URL 정의
url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EB%A7%A5%EB%B6%81"

# URL로 HTTP GET 요청 보내기
response = requests.get(url)

# 요청이 성공했는지 확인
if response.status_code == 200: #웹페이지 정상접속일 시 , 코드값이 200으로 나옴.
    # 페이지의 HTML 내용 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 블로그 글 정보가 포함된 요소 찾기
    post_items = soup.find_all('li', class_='bx')

    # 블로그 글 정보를 추출하고 출력
    for post_item in post_items:
        # 이전 코드
        # blog_name = post_item.find('a', class_='sh_blog_title').text
         blog_name = post_item.find('a', {'class': 'sh_blog_title'}).text

        blog_address = post_item.find('a', class_='sh_blog_title')['href']
        post_address = post_item.find('a', class_='sh_blog_title')['href']
        creation_date = post_item.find('dd', class_='txt_inline').text

        # 추출한 정보 출력
        print("블로그 명:", blog_name)
        print("블로그 주소:", blog_address)
        print("글의 주소:", post_address)
        print("작성일자:", creation_date)
        print("\n")
else:
    print("웹페이지를 가져오지 못했습니다. 상태 코드:", response.status_code)

from bs4 import BeautifulSoup
import urllib.request
import re
hdr = {'User-agent':'Mozilla/5.0(iPhone;CPU Iphone OS 10_3 like Mac OS X'}

f=open("c:\\work\\today.txt","wt",encoding='utf-8')

#페이징처리 추가 

for i in range(1,6):
    data = 'https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(i)
    print(data)

    req = urllib.request.Request(data, \
                                  headers = hdr)
    data = urllib.request.urlopen(req).read()
    page = data.decode('utf-8','ignore')
    soup = BeautifulSoup(page, 'html.parser')
    list = soup.find_all('td',attrs={'class' : 'subject'})
   
    #<td class="subject">
    #<a href="/board/view.php?table=bestofbest">
    #<\span> <\td>


    for item in list :
        try:
            title = item.find('a').text.strip()
            if re.search("미국",title):
              print(title)
              f.write(f"{title}\n")

        except :
            pass
        
f.close()

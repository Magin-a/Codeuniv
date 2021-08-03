import requests
from bs4 import BeautifulSoup

news_url = 'https://search.hankyung.com/apps.frm/search.news?query=코로나'

raw = requests.get(news_url)

# 문자열 타입의 HTML 코드 -> 실제 HTML 코드
# 이제 'BeautifulSoup' 라이브러리를 활용하여 'raw.text'를 실제 HTML 코드로 변환해줍니다.
soup = BeautifulSoup(raw.text, 'html.parser')

# 뉴스 기사를 모두 포함하는 큰 틀 지정
# 앞서 정의한 큰 틀의 태그는 <ul class="article"> 입니다.
# 'soup'에 저장된 HTML 코드에서 <ul class="article"> 태그를 찾아서 'box'라는 변수에 저장합니다.
box = soup.find('ul', {'class' : 'article'})


# 큰 틀에서 뉴스 기사의 제목만 추출
# 뉴스 기사 제목 10개는 <ul class="article"> 안에 있는 모든 <em class="tit"> 태그입니다.
# <ul class="article"> 태그에 있는 데이터가 모두 저장된 'box'에서 <em class="tit">에 해당하는
# 모든 데이터를 'all_title' 변수에 저장합니다.
all_tittle = box.find_all('em', {'class' : 'tit'})


# '코로나' 관련 뉴스 기사제목 10개 출력
# 지금까지 작성한 코드를 토대로, 'all_title'에 저장된 '코로나' 관련 뉴스 기사 제목 10개를 출력해보겠습니다.
for tittle in all_tittle:
    print(tittle.text.strip())





#7. 첫번째 기능 추가 - 여러 페이지의 뉴스 기사 제목수집

import requests
from bs4 import BeautifulSoup

for page in range(1, 11):
		# '문자열1' + '문자열2' = '문자열1문자열2'
		# 그냥 page를 url 주소와 더해주면 문자열+숫자 이므로 오류입니다.
		# 반드시 str(page)를 더해주세요!
    news_url = 'https://search.hankyung.com/apps.frm/search.news?query=코로나&page=' + str(page)
    raw = requests.get(news_url)

    soup = BeautifulSoup(raw.text, 'html.parser')

    box = soup.find('ul', {'class' : 'article'})
    all_title = box.find_all('em', {'class' : 'tit'})

		# 깔끔한 출력을 위한 수정
    print('<' + str(page) + '페이지 뉴스 기사 제목>')
    for title in all_title:
        t = title.text
        print(t.strip())
    print()



#9일차 ✅ 오늘의 문제: 한국경제뉴스 크롤링
# **⭐ 조건 ⭐**

# - '전체뉴스'가 아닌 '한국경제 뉴스' 크롤링
# - 본인이 관심 있는 키워드를 input()으로 입력받기
# - 출력 요소는 2개: 뉴스 기사 제목, 기사 작성 날짜 및 시간
# - 1, 2페이지의 뉴스 20개만 출력
# - 소스코드 및 출력 결과 인증


import requests
from bs4 import BeautifulSoup

count = 0
keyword = input()
for page in (1, 3):
    news_url = 'https://search.hankyung.com/apps.frm/search.news?query='+ keyword + '&page=' + str(page)
    raw = requests.get(news_url)

    soup = BeautifulSoup(raw.text, 'html.parser')

    box = soup.find('ul', {'class' : 'article'})
    all_tittle = box.find_all('em', {'class': 'tit'})
    all_time = box.find_all('span', {'class': 'date_time'})

    for tittle, time in zip(all_tittle, all_time):
        count += 1
        print(str(count)+'번'+' ' +tittle.text.strip()+": "+ time.text.strip())
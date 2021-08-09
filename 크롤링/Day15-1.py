#나의 
from selenium import webdriver
import time

keyword = input('뉴스 검색 키워드 : ')

driver = webdriver.Chrome('_win32/chromedriver.exe')
news_url = 'https://search.hankyung.com/apps.frm/search.news?query=' + keyword + '&mediaid_clust=HKPAPER,HKCOM'
driver.get(news_url)
time.sleep(2)



# 단순히 뉴스마다 번호를 붙여주기 위한 변수
cnt = 0

for i in range(1,4):
    news_url = 'https://search.hankyung.com/apps.frm/search.news?query='+ keyword +'&page='+str(i)
    driver.get(news_url)
    time.sleep(2)
    ten_articles = driver.find_elements_by_css_selector('em.tit')

    for article in ten_articles:

		# 'article'은 뉴스 기사 제목을 나타내는 HTML 요소이므로, text는 제목을 나타냄
      title = article.text

		# 'article'은 뉴스 기사 제목을 나타내는 HTML 요소이므로, 클릭하면 뉴스 기사 본문을 확인할 수 있음
      article.click()
		# 시간적 여유 원하는 만큼
      time.sleep(1)

		# 'driver'를 새로운 탭 (뉴스 기사 본문)으로 전환
      driver.switch_to.window(driver.window_handles[-1])

		# 기사 본문을 'content' 변수에 저장
      content = driver.find_element_by_id('articletxt').text

		# 기사 본문 출력
      cnt += 1
      print(f'< {cnt}번 뉴스 - {title} >')
      print(content)

		# 새로운 탭 (뉴스 기사 본문)에서 작업을 다 했으므로, 새로운 탭은 닫아줌
      driver.close()

		# 다시 'driver'를 맨 처음 탭으로 전환
      driver.switch_to_window(driver.window_handles[0])

		# 시간적 여유 원하는 만큼
      time.sleep(1)


# 크롬 창 닫기
driver.close()


#같은 조원 코드
# 라이브러리 import
from selenium import webdriver
import time

# 검색어 입력 키워드
keyword = input('뉴스 검색 키워드 : ' )

# 뉴스 기사 게시판 접속
driver  = webdriver.Chrome('_win32/chromedriver.exe')


# 단순히 뉴스마다 번호를 붙여주기 위한 변수 
count = 0

# 페이지 변수
for i in range(1,4):
    news_url = 'https://search.hankyung.com/apps.frm/search.news?query='+ keyword +'&page='+str(i)
    driver.get(news_url)
    time.sleep(2)

    # 모든 <em.tit> 태그를 'ten_articles'에 저장
    ten_articles = driver.find_elements_by_css_selector('em.tit')

    # 10개 뉴스기사를 대상으로 반복문 진행  
    for article in ten_articles : 
        # 'article'은 뉴스 기사 제목을 나타내는 HTML 요소이므로 , text는 제목을 나타냄
        title = article.text

        # 'article'은 뉴스 기사 제목을 나타내는 HTML 요소이므로, 클릭하면 본문기사를 확인할 수 있음. 
        article.click()
        time.sleep(1)

        # 'driver'를 새로운 탭 (뉴스 기사 본문) 으로 전환
        driver.switch_to.window(driver.window_handles[-1])

        # 기사 본문을 'content' 변수에 저장
        content = driver.find_element_by_id('articletxt').text
    
        # 기사를 줄별로 나눔
        separate = content.split('\n')

        # 기사 본문 출력
        count+=1
        print(f'<{count}번 뉴스 - {title} >')
        for sep in separate :
            if sep != '':
                print(sep, end = ' ')
        print('\n')

        # 새로운 탭 ( 뉴스 기사 본문 )에서 작업을 다 했으므로, 새로운 탭은 닫아줌
        driver.close()

        # 다시 'driver'를 맨 처음 탭으로 전환
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

# 크롬 창 닫기
driver.close()

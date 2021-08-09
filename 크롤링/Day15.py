from selenium import webdriver
import time

keyword = input("뉴스 키워드 검색 : ")

driver = webdriver.Chrome('_win32/chromedriver.exe')
url = 'https://search.hankyung.com/apps.frm/search.news?query='+ keyword +'&mediaid_clust=HKPAPER,HKCOM'
driver.get(url)

time.sleep(2)

articles = driver.find_elements_by_css_selector('em.tit')

cnt = 0
for _ in range(30):

    if cnt <10:
        articles = driver.find_elements_by_css_selector('em.tit')
        for article in articles:
            title = article.text
        
        # 각 기사의 본문을 확인하기 위해서 클릭
            article.click()
            time.sleep(2)
    
    	# 'driver'를 새로운 탭 (뉴스 기사 본문)으로 전환
            driver.switch_to.window(driver.window_handles[-1])

        # 기사 본문을 'content' 변수에 저장
            content = driver.find_element_by_id('articletxt').text
    	# 기사 본문 출력
            cnt += 1
            print('\n' +'< {0}번 뉴스 - {1} >'.format(cnt, title))
            print(content)

		# 새로운 탭 (뉴스 기사 본문)에서 작업을 다 했으므로, 새로운 탭은 닫아줌
            driver.close()
    
		# 다시 'driver'를 맨 처음 탭으로 전환
            driver.switch_to_window(driver.window_handles[0])
   

		# 시간적 여유 원하는 만큼
            time.sleep(1)



    elif cnt == 10:
        
        driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[2]/div/span/a[1]').click()
        articles = driver.find_elements_by_css_selector('em.tit')
        for article in articles:
            title = article.text
        
        # 각 기사의 본문을 확인하기 위해서 클릭
            article.click()
            time.sleep(2)
    
    	# 'driver'를 새로운 탭 (뉴스 기사 본문)으로 전환
            driver.switch_to.window(driver.window_handles[-1])

        # 기사 본문을 'content' 변수에 저장
            content = driver.find_element_by_id('articletxt').text
    	# 기사 본문 출력
            cnt += 1
            print('\n' +'< {0}번 뉴스 - {1} >'.format(cnt, title))
            print(content)

		# 새로운 탭 (뉴스 기사 본문)에서 작업을 다 했으므로, 새로운 탭은 닫아줌
            driver.close()
    
		# 다시 'driver'를 맨 처음 탭으로 전환
            driver.switch_to_window(driver.window_handles[0])
   

		# 시간적 여유 원하는 만큼
            time.sleep(1)


    elif cnt == 20:
        
        driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[2]/div/span/a[2]').click()
        articles = driver.find_elements_by_css_selector('em.tit')
        for article in articles:
           title = article.text
        
        # 각 기사의 본문을 확인하기 위해서 클릭
           article.click()
           time.sleep(2)
    
    	# 'driver'를 새로운 탭 (뉴스 기사 본문)으로 전환
           driver.switch_to.window(driver.window_handles[-1])

        # 기사 본문을 'content' 변수에 저장
           content = driver.find_element_by_id('articletxt').text
    	# 기사 본문 출력
           cnt += 1
           print('\n' +'< {0}번 뉴스 - {1} >'.format(cnt, title))
           print(content)

		# 새로운 탭 (뉴스 기사 본문)에서 작업을 다 했으므로, 새로운 탭은 닫아줌
           driver.close()
    
		# 다시 'driver'를 맨 처음 탭으로 전환
           driver.switch_to_window(driver.window_handles[0])
   

		# 시간적 여유 원하는 만큼
        time.sleep(1)
        
    

# 크롬 창 닫기
driver.close()



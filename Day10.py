#1. 필요한 라이브러리 import 
from selenium import webdriver
import time

# 2.  자동화된 크롬 창 실행

driver = webdriver.Chrome('_win32/chromedriver.exe')
my_url1 = 'https://naver.com/'
driver.get(my_url1)
#코드 설명)
# 추가된 한 줄을 해석해보자면, 'webdriver'에 'chromedriver.exe'를 연결한 객체를 생성하여 
# 수 'driver'에 저장한다는 뜻입니다. 저는 처음 공부했을 때 이게 무슨 말인가 싶었는데😫
# 가상의 크롬 창을 열 수 있도록 도와주는 속성값과 행동들을 'driver'라는 변수에 넣는다고 생각해주세요!
# ​

# 그리고 코드 맨 뒤의 괄호 안에 적힌 './chromedriver'는 아래 사진과 같이 '소스코드와 같은 위치 (폴더)에 있는 chromedriver.exe를 사용한다'는 뜻입니다.

# 만약 다른 폴더에 저장해두셨다면 파일 경로를 직접 작성해주셔야 해요.
# 같은 폴더에 저장해주시는게 편합니다🙂


#3. 시간적 여유 넣기
time.sleep(10) #3초의 시간적 여유

#4. 크롬 창 닫기
driver.close()



#실습
from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/박영웅/Desktop/python연습장/이온2파이썬/코뮤니티/크롤링/chromedriver_win32/chromedriver.exe')
my_url = 'https://naver.com/'
driver.get(my_url)

time.sleep(10)
driver.find_element_by_css_selector('input#query.input_text').send_keys('코로나')
driver.find_element_by_css_selector('button#search_btn').click()

driver.close()

#게임(홈페이지) 자동로그인
from selenium import webdriver
import time

driver = webdriver.Chrome('_win32/chromedriver.exe')
my_url = 'https://maplestory.nexon.com/Authentication/Login'
driver.get(my_url)



driver.find_element_by_css_selector('input#eid').send_keys('')
driver.find_element_by_css_selector('input#epw').send_keys('')
driver.find_element_by_css_selector('div#wrap > div.wrapper > div > div.login_form01 > div.login_btn_wrap').click()
# driver.find_element_by_css_selector('button#layerMovie > div > button.btn.btn_hide').click()
# driver.find_element_by_css_selector('button#header > div > ul > li.btn_c > button').click()

# driver.find_element_by_css_selector('a#section02 > div > span > div > a').click()

time.sleep(10)
driver.close()
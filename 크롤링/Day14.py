from selenium import webdriver
import time

driver = webdriver.Chrome('_win32/chromedriver.exe')
url = 'https://cafe.naver.com/codeuniv'
driver.get(url)
time.sleep(2)


for i in range(20):
    driver.find_element_by_css_selector('a#main-area > div:nth-child(6) > table > tbody > tr:nth-child(1) > td.td_article > div.board-list > div > a')

# **⭐ 조건 ⭐**

# 1. `영단어 입력 - 번역 버튼 클릭 - 번역 결과 수집 - 입력 칸 초기화` 과정을 
# 하나의 함수로 정의하기
#     - 함수 이름 : get_papago_result
#     - 입력 변수 : 1개 (영단어)
#     - 리턴 값 : 번역 결과
# 2. 반복문을 활용하여 번역 5회 진행
# 3. 번역 사전 'my_dict' 출력

from selenium import webdriver
import time

my_dict = {}

driver = webdriver.Chrome('_win32/chromedriver.exe')
my_url = 'https://papago.naver.com/'
driver.get(my_url)
time.sleep(3)

def get_papago_result(words):
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(words)
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)
    output = driver.find_element_by_css_selector('div#targetEditArea').text
    driver.find_element_by_css_selector('textarea#txtSource').clear()
    return output


for _ in range(5):
    my_word = input("번역할 영단어 입력 : ")
    my_dict[my_word] = get_papago_result(my_word)

    

print(my_dict)
driver.close()


import time
from selenium import webdriver

my_dict = {}


url = "https://papago.naver.com/"

driver = webdriver.Chrome('_win32/chromedriver.exe')
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
##################
driver.get(url)
# 시간적 여유
time.sleep(3)



def get_papago_result(question):
    # 번역할 데이터 입력
    driver.find_element_by_css_selector("textarea#txtSource").send_keys(question)
    # 번역하기 버튼 클릭
    driver.find_element_by_css_selector("button#btnTranslate").click()
    time.sleep(1)
    # 번역데이터 가져오기
    output = driver.find_element_by_css_selector("div#targetEditArea").text
    # 입력값 초기화
    driver.find_element_by_css_selector("textarea#txtSource").clear()
    return output

for i in range(5):
# 영단어 입력받기
    question = input("번역하고 싶은 영단어 입력 : ")
    my_dict[question] = get_papago_result(question)
   
print(my_dict)
# 크롬 창 닫기
driver.close()




import csv

count = 0

f = open('C:\Users\박영웅\Downloads./covid19_articles.csv', 'r')
rdr = csv.reader(f)

next(rdr)

for row in rdr :
    if '[속보]' in row[2] :
        print(row[2])
        count += 1
        
f.close()
print ("속보 기사 개수 :",count)



import csv

f=open('covid19_articles.csv','r', encoding = 'euc-kr')


rdr=csv.reader(f)

count=0
for row in rdr:
    if '[속보]' in row[2]:
        print(row[2])
        count=count+1

f.close()
print('속보 기사 개수:',str(count))

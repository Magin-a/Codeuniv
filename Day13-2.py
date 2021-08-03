from selenium import webdriver
import time
import csv

#크롬창 실행
driver = webdriver.Chrome('_win32/chromedriver.exe')
papago_url = 'https://papago.naver.com/'

driver.get(papago_url)

#작성할 파일 생성
f = open('my_papago_practice.csv', 'w', newline = '')

#4. 작성하는 객체 변수 생성
# 'writer' 객체를 사용하면 CSV 파일을 직접 작성할 수 있다고 설명드렸습니다.
# 'writer' 객체의 기능을 갖는 변수 'wtr'을 생성해줍니다.
# CSV 파일을 작성하는 객체 변수 'wtr' 생성
wtr = csv.writer(f)

# 열 제목 작성
wtr.writerow(['영단어', '번역결과'])

while True:
    keyword = input('번역할 단어를 입력 (0을 입력하면 종료) : ')
    if keyword == '0':
        print("번역종료")
        break

    # 영단어 입력, 번역 버튼 클릭
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(keyword)
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)
    output = driver.find_element_by_css_selector('div#txtTarget').text
    
    # my_papago.csv 파일에 [영단어, 번역결과] 작성
    wtr.writerow([keyword, output])

    # 영단어 입력 칸 초기화
    driver.find_element_by_css_selector('textarea#txtSource').clear()




#일일 과제 역으로 번역하기
#크롬창 실행
driver = webdriver.Chrome('_win32/chromedriver.exe')
papago_url = 'https://papago.naver.com/'
my_word = []
driver.get(papago_url)
time.sleep(1)

f = open('my_papago_practice.csv', 'r')
rdr = csv.reader(f)
next(rdr)

for i in rdr:
   my_word.append(i[1])
f.close()

f2 = open('my_papago_practice2.csv', 'w', newline = '')
wtr = csv.writer(f2)


for keyword in my_word:
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(keyword)
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(2)
    output = driver.find_element_by_css_selector('div#txtTarget').text
    wtr.writerow([keyword, output])
    driver.find_element_by_css_selector('textarea#txtSource').clear()
time.sleep(3)
driver.close()
f2.close()

f = open('my_papago_practice2.csv', 'r')
rdr = csv.reader(f)

for i in rdr:
    print(i[0]+':'+ i[1])
f.close()
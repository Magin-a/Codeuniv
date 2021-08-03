# from selenium import webdriver
# import time
# import csv

# driver = webdriver.Chrome('C:/Users/박영웅/Desktop/python연습장/이온2파이썬/코뮤니티/크롤링/chromedriver_win32/chromedriver.exe')
# my_url = 'https://papago.naver.com/'
# driver.get(my_url)

# time.sleep(2)

# f = open('./mypapago.csv1', 'w', newline = '')

# #4. 작성하는 객체 변수 생성
# # 'writer' 객체를 사용하면 CSV 파일을 직접 작성할 수 있다고 설명드렸습니다.
# # 'writer' 객체의 기능을 갖는 변수 'wtr'을 생성해줍니다.
# wtr = csv.writer(f)


# #5. CSV 파일의 열 제목 작성  
# # 실질적인 데이터 (영단어, 번역 결과)를 CSV 파일에 작성하기 전, 먼저 열의 제목을 작성해줍니다.
# # 열 제목 작성
# wtr.writerow(['영단어', '번역결과'])

# #6. 반복문을 활용하여 번역 여러 번 실행 및 CSV 파일에 저장  
# # 번역 작업을 원하는 만큼 실행할 수 있도록 무한 루프를 사용해보겠습니다.
# # ​
# # 만약 영단어 대신 '0'을 입력하면, 무한 루프를 중지시킵니다.


# # 무한 루프
# while True:
#     keyword = input('번역할 영단어 입력 (0 입력하면 종료) : ')
#     if keyword == '0':
#         print('번역 종료')
#         break

#     # 영단어 입력, 번역 버튼 클릭
#     driver.find_element_by_css_selector('textarea#txtSource').send_keys(keyword)
#     driver.find_element_by_css_selector('button#btnTranslate').click()
#     time.sleep(1)

# 	# 번역 결과 저장
#     output = driver.find_element_by_css_selector('div#txtTarget').text
    
# 	# my_papago.csv 파일에 [영단어, 번역결과] 작성
#     wtr.writerow([keyword, output])
    
# 	# 영단어 입력 칸 초기화
#     driver.find_element_by_css_selector('textarea#txtSource').clear()

# # 크롬 창 닫기
# driver.close()

# # 파일 닫기
# f.close()

#오늘의 과제
# from selenium import webdriver
# import time
# import csv

# my_word = []

# driver = webdriver.Chrome('C:/Users/박영웅/Desktop/python연습장/이온2파이썬/코뮤니티/크롤링/chromedriver_win32/chromedriver.exe')
# my_url = 'https://papago.naver.com/'
# driver.get(my_url)

# time.sleep(2)

# # #영어↔한국어 버튼 한번만 누르기
# # driver.find_element_by_css_selector('button.btn_switch___x4Tcl').click()

# f = open('mypapago.csv1', 'r')
# rdr = csv.reader(f)
# next(rdr)

# for i in rdr:
#     my_word.append(i[1])

# f.close()


# f2 = open('mypapago_re.csv', 'w', newline = '')
# wtr = csv.writer(f2)

# for y in my_word:
#     driver.find_element_by_css_selector('textarea#txtSource').send_keys(y)
#     driver.find_element_by_css_selector('button#btnTranslate').click()
#     time.sleep(2)

#     output = driver.find_element_by_css_selector('div#txtTarget').text
#     time.sleep(1)
#     wtr.writerow([i[1], output])
#     driver.find_element_by_css_selector('textarea#txtSource').clear()

# driver.close()
# f2.close()

# #결과
# f = open('./mypapago_re.csv', 'r')
# rdr = csv.reader(f)

# for row in rdr:
#     print(row[0], row[1])

# f.close()

from selenium import webdriver
import time
import csv

# 크롬창 생성 및 원하는 링크로 이동
url = 'https://papago.naver.com/'
driver = webdriver.Chrome('C:/Users/박영웅/Desktop/python연습장/이온2파이썬/코뮤니티/크롤링/chromedriver_win32/chromedriver.exe')
driver.get(url)
time.sleep(3)

# 기존의 파일 불러오기
f1 = open('./mypapago.csv1', 'r')
rdr = csv.reader(f1)
next(rdr)

my_dict_val = []

# 저장된 값들 중 번역 결과를 my_dict_val에 저장
for row in rdr:
    my_dict_val.append(row[1])

f1.close()

f_new = open('./my_papago_re.csv', 'w', newline = '')
wtr = csv.writer(f_new)

for i in my_dict_val:
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(i) # 단어 입력
    driver.find_element_by_css_selector('button#btnTranslate').click() # 번역 버튼 클릭
    time.sleep(2)

    output = driver.find_element_by_css_selector('div#txtTarget').text # 번역 결과 값 가져오기

    wtr.writerow([i, output])
    
    driver.find_element_by_css_selector('textarea#txtSource').clear() # 입력창 초기화

driver.close()
f_new.close()

# 결과 확인
f = open('./my_papago_re.csv', 'r')
rdr = csv.reader(f)

for row in rdr:
    print(row[0], row[1])

f.close()

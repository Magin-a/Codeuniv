# 3. 아이디 & 비밀번호 입력
# 이제 아이디와 비밀번호를 입력해줍니다.
# 아까 말씀드렸지만, 네이버에 로그인 할 경우 'send_keys()' 함수가 아니라 'execute_script()' 함수를 사용합니다.

from selenium import webdriver
import time

cnt = 1
driver = webdriver.Chrome('win32/chromedriver.exe')
login_url = 'https://nid.naver.com/nidlogin.login'
driver.get(login_url)
time.sleep(2)

# 본인의 아이디, 비밀번호를 각각 변수에 저장
# ex) 아이디 : comu, 비밀번호 : 12345
my_id = ''
my_pw = ''

# 아이디와 비밀번호 입력
driver.execute_script("document.getElementsByName('id')[0].value = \'" + my_id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value = \'" + my_pw + "\'")

# 시간적 여유 원하는 만큼
time.sleep(1)

# '로그인' 버튼 클릭
driver.find_element_by_css_selector('label#label_login_chk').click()
driver.find_element_by_id('log.login').click()

# 시간적 여유 원하는 만큼
time.sleep(5)

# 코뮤니티 접속
comu_url = 'https://cafe.naver.com/codeuniv'
driver.get(comu_url)

# 시간적 여유 원하는 만큼
time.sleep(1)

# '신규회원게시판' 클릭
driver.find_element_by_id('menuLink90').click()

# 시간적 여유 원하는 만큼
time.sleep(1)

# 프레임 전환
driver.switch_to.frame('cafe_main')

# 시간적 여유 원하는 만큼
time.sleep(1)

# 첫번째 글 클릭
driver.find_element_by_xpath('//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a').click()

# 시간적 여유 원하는 만큼
time.sleep(1)

content = driver.find_element_by_css_selector('div.se-component-content').text
print("{} 번째 글>".format(cnt))
print(content + '\n')

for _ in range(19):
    driver.find_element_by_css_selector('a.BaseButton.btn_next.BaseButton--skinGray.size_default').click()
    time.sleep(2)
    content = driver.find_element_by_css_selector('div.se-component-content').text
    cnt += 1
    print("<{} 번째 글>".format(cnt))
    print(content + '\n')

driver.close()


from selenium import webdriver
import time

naver_url = 'https://www.naver.com/'
driver = webdriver.Chrome('_win32/chromedriver.exe')
driver.get(naver_url)
time.sleep(3)

# 로그인 페이지 접속
driver.find_element_by_xpath('//*[@id="account"]/a').click()
time.sleep(2)

# 로그인
my_id = 'yg990828'
my_pw = 'magin9580'

driver.execute_script("document.getElementsByName('id')[0].value = \'" + my_id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value = \'" + my_pw + "\'")
time.sleep(1)

driver.find_element_by_css_selector('label#label_login_chk').click()
driver.find_element_by_id('log.login').click()
time.sleep(5)

# 코뮤니티로 이동
comu_url = 'https://cafe.naver.com/codeuniv'
driver.get(comu_url)
time.sleep(2)

# 게시판으로 이동
driver.find_element_by_id('menuLink90').click()
time.sleep(1)

# 프레임
driver.switch_to.frame('cafe_main')
time.sleep(1)

# 첫 게시글으로 이동 및 내용 프린트
driver.find_element_by_xpath('//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a').click()
time.sleep(1)

content = driver.find_element_by_css_selector('div.se-component-content').text

count = 1

print('<{}번째 게시물 내용>'.format(count))
print(content + '\n')

# 반복추출
for i in range(19):
    count += 1

    driver.find_element_by_css_selector('a.BaseButton.btn_next.BaseButton--skinGray.size_default').click()
    time.sleep(1)
    
    content = driver.find_element_by_css_selector('div.se-component-content').text

    print('<{}번째 게시물 내용>'.format(count))
    print(content + '\n')

driver.close()

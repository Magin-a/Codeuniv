from bs4 import BeautifulSoup
import requests

lotto_url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
raw = requests.get(lotto_url)

soup = BeautifulSoup(raw.text, 'html.parser')

#우리가 필요한 정보의 큰 틀 
box = soup.find('div', {'class' : 'nums'})

#필요한 정보 (<div class="nums"> 안에 있는 모든 <span> 태그)
numbers = box.find_all('span')

print('< 최근 로또 당첨 번호')
for number in numbers:
    print(number.text)

    

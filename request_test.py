from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

import requests

from bs4 import BeautifulSoup as bs

from time import sleep

driver = webdriver.Chrome(r'C:\chromedriver.exe')

driver.implicitly_wait(3)

driver.get('https://www.4nb.co.kr/v2/index.php')
driver.maximize_window()

wait = WebDriverWait(driver,10)

html = driver.page_source

soup = bs(html,'html.parser')


#위 html 주소 = 4nb 홈페이지를 불러온 후
#bs4 를 이용하여 해당 사이트의 모든 소스코드를 가져온다.

#이후 아래에서는 가져온 소스코드에서 a태그의 href, area태그의 href를 불러와
#http://help.4nb.co.kr에 합쳐준다.
#합쳐진 url을 request한 뒤 response값을 받는다.
#이 때, 200을 제외한 나머지는 모두 에러로 취급하여 콘솔에 표시한다.


# a태그
print('a sector')
for a in soup.find_all('a', href=True):
      if a['href'] == 'http://help.4nb.co.kr':
            print(a['href'])
            url = a['href']
            response = requests.get(url)
            print("result: ",response.status_code)
            if response.status_code != 200:
                  print("error url: ",url)
                  print("error code:",response.status_code)
      elif a['href'].find('v2')==-1:
            print("https://www.4nb.co.kr/"+a['href'])
            url = "https://www.4nb.co.kr/v2/"+a['href']
            response = requests.get(url)
            print("result: ",response.status_code)
            if response.status_code != 200:
                  print("error url: ",url)
                  print("error code:",response.status_code)
      else:
            print("https://www.4nb.co.kr/"+a['href'])
            url = "https://www.4nb.co.kr/"+a['href']
            response = requests.get(url)
            print("result: ",response.status_code)
            if response.status_code != 200:
                  print("error url: ",url)
                  print("error code:",response.status_code)

# area태그
print('area sector')
for area in soup.find_all('area', href=True):
      if area['href'] == 'http://help.4nb.co.kr':
            print(area['href'])
            url = area['href']
            response = requests.get(url)
            print("result: ",response.status_code)
            if response.status_code != 200:
                  print("error url: ",url)
                  print("error code:",response.status_code)
      elif area['href'].find('v2')==-1:
            print("https://www.4nb.co.kr/"+area['href'])
            url = "https://www.4nb.co.kr/v2/"+area['href']
            response = requests.get(url)
            print("result: ",response.status_code)
            if response.status_code != 200:
                  print("error url: ",url)
                  print("error code:",response.status_code)
      else:
            print("https://www.4nb.co.kr/"+area['href'])
            url = "https://www.4nb.co.kr/"+area['href']
            response = requests.get(url)
            print("result: ",response.status_code)
            if response.status_code != 200:
                  print("error url: ",url)
                  print("error code:",response.status_code)


sleep(3) 

driver.quit()

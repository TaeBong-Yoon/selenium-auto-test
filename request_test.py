import requests
from bs4 import BeautifulSoup as bs
import re

req = requests.get('https://www.4nb.co.kr/v2/index.php')
raw = req.text

text = re.sub('<!-.+?->','',raw,0,re.I|re.S)

html = bs(text, 'html.parser')

soup = html.find('body')

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

def run(url,requests,bs,re):
      req = requests.get(url)
      raw = req.text

      #주석 잘라내기
      text = re.sub('<!-.+?->','',raw,0,re.I|re.S)

      html = bs(text, 'html.parser')

      soup = html.find('body')

      # a태그
      print('a sector')
      for a in soup.find_all('a', href=True):
            #help.4nb.co.kr 경로 처리
            if a['href'].find('help') >-1 :
                  url = a['href']
                  response = requests.get(url)
                  if response.status_code != 200:
                        print("error url: ",url)
                        print("error code:",response.status_code)
                  else:
                        print(url)
                        print("result: ",response.status_code)
            #../로 되어있는 경로 처리
            elif a['href'].find('..')>-1:
                  url = "https://www.4nb.co.kr/v2/"+a['href'].replace('..','')
                  response = requests.get(url)
                  if response.status_code != 200:
                        print("error url: ",url)
                        print("error code:",response.status_code)
                  else:
                        print(url)
                        print("result: ",response.status_code)
            #v2/가 없는 경로 처리
            elif a['href'].find('v2')==-1:
                  url = "https://www.4nb.co.kr/v2/"+a['href']
                  response = requests.get(url)
                  if response.status_code != 200:
                        print("error url: ",url)
                        print("error code:",response.status_code)
                  else:
                        print(url)
                        print("result: ",response.status_code)
            else:
                  url = "https://www.4nb.co.kr/"+a['href']
                  response = requests.get(url)
                  if response.status_code != 200:
                        print("error url: ",url)
                        print("error code:",response.status_code)
                  else:
                        print(url)
                        print("result: ",response.status_code)

      # area태그
      print('area sector')
      for area in soup.find_all('area', href=True):
            if area['href'].find('help') >-1 :
                  url = area['href']
                  response = requests.get(url)
                  if response.status_code != 200:
                        print("error url: ",url)
                        print("error code:",response.status_code)
                  else:
                        print(url)
                        print("result: ",response.status_code)
            elif a['href'].find('..')>-1:
                  url = "https://www.4nb.co.kr/v2/"+a['href'].replace('..','v2')
                  response = requests.get(url)
                  if response.status_code != 200:
                        print("error url: ",url)
                        print("error code:",response.status_code)
                  else:
                        print(url)
                        print("result: ",response.status_code)
            elif area['href'].find('v2')==-1:
                  url = "https://www.4nb.co.kr/v2/"+area['href']
                  response = requests.get(url)
                  if response.status_code != 200:
                        print("error url: ",url)
                        print("error code:",response.status_code)
                  else:
                        print(url)
                        print("result: ",response.status_code)
            else:
                  url = "https://www.4nb.co.kr/"+area['href']
                  response = requests.get(url)
                  if response.status_code != 200:
                        print("error url: ",url)
                        print("error code:",response.status_code)
                  else:
                        print(url)
                        print("result: ",response.status_code)
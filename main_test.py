from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

from time import sleep

driver = webdriver.Chrome(r'C:\chromedriver.exe')

driver.implicitly_wait(3)

driver.get('https://www.4nb.co.kr/v2/index.php')
driver.maximize_window()

wait = WebDriverWait(driver,10)

def go_back():
      sleep(0.5)
      driver.execute_script("window.history.go(-1)")
      sleep(0.5)

#go_back() 사용 후 값이 새로고쳐져야 하므로 action을 계속해서 갱신(?)해준다.
def drop_down():
      action=ActionChains(driver)
      mainmenu = driver.find_element(By.XPATH,'//*[@id="mainmenu"]/li[1]')
      action.move_to_element(mainmenu).perform()

def accept_alert():
      sleep(0.5)
      Alert(driver).accept()
      sleep(0.5)

#메인 logo
print('logo test...')
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="logo"]'))).click()

#메인메뉴 maimmenu
print('mainmenu test...')

for i in range(1,5):
      for j in range(1,6):
                  if i==2 and j==4:
                        break
                  elif i==4 and j==5:
                        break
                  drop_down()
                  wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="top"]/nav/div/div/div/div['+str(i)+']/ul/li['+str(j)+']/a'))).click()
                  go_back()

for k in range(1,4):
      drop_down()
      wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="top"]/nav/div/div/div/div[1]/ul/li[1]/ul/li['+str(k)+']/a'))).click()
      go_back()
      
#고객지원 센터
print('help center test...')

wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="top"]/p/a'))).click()
sleep(0.5)

##새로 열린창 닫은 후
driver.switch_to.window(driver.window_handles[1])
driver.close()
##원래 창으로 이
driver.switch_to.window(driver.window_handles[0])
sleep(0.5)

driver.refresh()

#상단 슬라이드 carouselController
print('carousel test...')

wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="carouselController"]/div/button/i'))).click()

for i in range(1,3):
      for j in range(1,4):
            wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="carouselController"]/li['+str(i)+']'))).click()
            #url을 읽어와야함, 
            sleep(0.5)
            wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/map['+str(i)+']/area['+str(j)+']'))).click()
            go_back()

for i in range(3,5):
      for j in range(1,3):
            if i==3:
                  wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="carouselController"]/li['+str(i)+']'))).click()
                  sleep(0.5)
                  wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/map['+str(i+1)+']/area['+str(j)+']'))).click()
                  go_back()
            else:
                  wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="carouselController"]/li['+str(i)+']'))).click()
                  sleep(0.5)
                  wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/map['+str(i-1)+']/area['+str(j)+']'))).click()
                  go_back()



#중간카테고리 linkarea
print('linkarea test...')

for i in range(1,7):

    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="linkarea"]/ul/li['+str(i)+']/a/img'))).click()
    go_back()
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="linkarea"]/ul/li['+str(i)+']/a/span'))).click()
    go_back()

#제품문의 cs
print('cs test...')

wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="cs"]/p[2]/a'))).click()
go_back()

#공급현황 supply
print('supply test...')

#####more
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="supply"]/h2/span[2]/a'))).click()
go_back()

#####list
for i in range(1,9):
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="supply"]/ul/li['+str(i)+']/a'))).click()
        go_back()

#공지사항 notice
print('notice test...')

#####more
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="notice"]/h2/span[2]/a'))).click()
go_back()

#####list
for i in range(1,3):
    if i==1:
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="notice"]/ul/li[1]/a/strong/font'))).click()
    else:
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="notice"]/ul/li['+str(i)+']/a'))).click()
    go_back()


#제품/가격문의 skybox

writer = driver.find_element(By.ID,'writer')
company = driver.find_element(By.ID,'company')
tel = driver.find_element(By.ID,'tel')
email = driver.find_element(By.ID,'email')
content = driver.find_element(By.ID,'content')

wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="form_4nb"]/div[6]/button'))).click()
accept_alert()

writer.send_keys('for\ue00dtest')
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="form_4nb"]/div[6]/button'))).click()
accept_alert()

company.send_keys('test\ue00dcompany')
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="form_4nb"]/div[6]/button'))).click()
accept_alert()

tel.send_keys('010-0000-0000')
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="form_4nb"]/div[6]/button'))).click()
accept_alert()

email.send_keys('test@test.com')
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="form_4nb"]/div[6]/button'))).click()
accept_alert()

content.send_keys(
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam eget dapibus mauris. Vivamus risus massa, luctus congue porta at, venenatis sodales erat. Nullam cursus velit non nisi sagittis accumsan. Pellentesque quis magna a urna volutpat ornare.')

sleep(0.5)

writer.clear()
company.clear() 
tel.clear()
email.clear()
content.clear()

#배너 banner
print('banner test...')

for i in range(1,2):
      wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="banner"]/div['+str(i)+']/h2/strong/a'))).click()
      go_back()

#상담신청 버튼 container
print('container test...')

wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/article[3]/p[2]/a/img'))).click()
go_back()

#고객사 목록 reference
print('reference test...')

for i in range(1,5):
      wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="reference"]/ul/li['+str(i)+']/a'))).click()
      go_back()

#하단메뉴 footer
print('footer test...')

for i in range(1,5):
      wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="footer01_ch_new"]/div/div[2]/div/p['+str(i)+']/a'))).click()
      go_back()

for i in range(2,6):
      for j in range(2,7):
            if i==2 and j==6:
                  break
            elif i==3 and j==5:
                  break
            elif i==5 and j==6:
                  break
            else:
                  wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="footer01_ch_new"]/div/div['+str(i)+']/p['+str(j)+']/a'))).click()
                  go_back()

sleep(3) 

driver.quit()































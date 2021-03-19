from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

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

#메인 logo
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="logo"]'))).click()

#메인메뉴 maimmenu
for i in range(1,6):
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
        

sleep(3) 

driver.quit()

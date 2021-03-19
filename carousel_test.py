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


wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="carouselController"]/div/button/i'))).click()

for i in range(1,3):
      for j in range(1,4):
            wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="carouselController"]/li['+str(i)+']'))).click()
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

sleep(3) 

driver.quit()

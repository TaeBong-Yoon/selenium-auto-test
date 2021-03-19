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

def run(driver,wait,By,EC,ActionChains,sleep):
      def go_back():
            sleep(0.5)
            driver.execute_script("window.history.go(-1)")
            sleep(0.5)
            
            #footer1 제품소개
            for i in range(1,5):
                  wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="footer01_ch_new"]/div/div[2]/div/p['+str(i)+']/a'))).click()
                  go_back()
            #footer1 제품문의~회사소개
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
            #footer2 Email href                        
            wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="footer02_ch_new"]/div/div[2]/div[1]/div[3]/p[2]/a'))).click()
            go_back()
            sleep(3)
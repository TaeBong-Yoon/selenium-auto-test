def run(driver,wait,By,EC,ActionChains,sleep):
      def go_back():
            sleep(0.5)
            driver.execute_script("window.history.go(-1)")
            sleep(0.5)

      #go_back() 사용 후 값이 새로고쳐져야 하므로 action을 계속해서 갱신(?)해준다.
      def drop_down():
            action=ActionChains(driver)
            mainmenu = driver.find_element(By.XPATH,'//*[@id="mainmenu"]/li[1]')
            action.move_to_element(mainmenu).perform()

      #logo
      wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="logo"]'))).click()

      #top nav
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

      wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="top"]/p/a'))).click()
      sleep(0.5)

      ##새로 열린창(help.4nb.co.kr) 닫은 후
      driver.switch_to.window(driver.window_handles[1])
      driver.close()
      ##원래 창으로 이동
      driver.switch_to.window(driver.window_handles[0])
      sleep(0.5)

      sleep(3)
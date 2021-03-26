def run(driver,wait,By,EC,ActionChains,sleep,Alert):
      def accept_alert():
            sleep(0.5)
            Alert(driver).accept()
            sleep(0.5)

      print('input test...')

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

      sleep(3)
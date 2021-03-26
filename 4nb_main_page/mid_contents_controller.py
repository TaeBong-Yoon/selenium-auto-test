def run(driver,wait,By,EC,ActionChains,sleep):
    def go_back():
      sleep(0.5)
      driver.execute_script("window.history.go(-1)")
      sleep(0.5)

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

    sleep(3)
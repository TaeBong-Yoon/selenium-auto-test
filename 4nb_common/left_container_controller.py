def run(driver,wait,By,EC,ActionChains,sleep,category):
    def go_back():
            sleep(0.5)
            driver.execute_script("window.history.go(-1)")
            sleep(0.5)

    if category == 'products':
        for i in range(1,6):
            wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="leftmenu"]/ul/li['+str(i)+']/a'))).click()
            go_back()
        for i in range(1,4):
            wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="leftmenu"]/ul/li[1]/ul/li['+str(i)+']/a'))).click()
            go_back()
    elif category == 'inquiry':
        for i in range(1,4):
            wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="leftmenu"]/ul/li['+str(i)+']/a'))).click()
            go_back()
    elif category == 'customers':
        for i in range(1,6):
            wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="leftmenu"]/ul/li['+str(i)+']/a'))).click()
            go_back()
    elif category == 'aboutus':
        for i in range(1,5):
            wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="leftmenu"]/ul/li['+str(i)+']/a'))).click()
            go_back()
    
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="call"]/p[4]/a'))).click()
    go_back()
    for i in range(1,3):
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="call"]/ul/li['+str(i)+']/a'))).click()
        go_back()
    for i in range(1,4):
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="faq"]/ul/li['+str(i)+']/a'))).click()

    go_back()
    sleep(3)
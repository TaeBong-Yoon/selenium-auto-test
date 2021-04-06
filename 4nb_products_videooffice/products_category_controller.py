def run(driver,wait,By,EC,ActionChains,sleep):
    def go_back():
        sleep(0.5)
        driver.execute_script("window.history.go(-1)")
        sleep(0.5)
    
#videooffice.php
    #화상회의 기술소개
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="contents"]/div[9]/p[2]/a/img'))).click()
    go_back()
    #화상회의 제품스냅샷
    for i in range(1,8):
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="contents"]/div[10]/div[2]/div[1]/img'))).click()
        sleep(0.5)
    for i in range(1,8):
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="contents"]/div[10]/div[2]/div[3]/img'))).click()
        sleep(0.5)
    #화상회의 도입방법
    for i in range(1,3):
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="boxall"]/div['+str(i)+']/p[2]/a/img'))).click()
        go_back()
    #화상회의 구매장비 안내
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="contents"]/div[13]/p[1]/a'))).click()
    go_back()
    #제품소개서 다운로드
    for i in range(1,3):
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="contents"]/div[14]/div/p['+str(i)+']/a/img'))).click()
        go_back()
    
    driver.get('https://www.4nb.co.kr/v2/introduction/onpremise.php')
    sleep(1)

#introduction.php
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="tab"]/ul/li[2]/a'))).click()
    go_back() 

    driver.get('https://www.4nb.co.kr/v2/products/videoschool.php')
    sleep(1)

#videoschool.php
    #화상강의 기술소개
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="contents"]/div[9]/p[3]/a/img'))).click()
    go_back()
    #화상강의 제품스냅샷
    for i in range(1,8):
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="contents"]/div[10]/div[2]/div[1]/img'))).click()
        sleep(0.5)
    for i in range(1,8):
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="contents"]/div[10]/div[2]/div[3]/img'))).click()
        sleep(0.5)    
    #화상회의 도입방법
    for i in range(1,3):
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="boxall"]/div['+str(i)+']/p[2]/a/img'))).click()
        go_back()
    #제품소개서 다운로드
    for i in range(1,3):
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="contents"]/div[14]/div/p['+str(i)+']/a/img'))).click()
        go_back()

    driver.get('https://www.4nb.co.kr/v2/products/webinar.php')
    sleep(2)
    
#webinar.php
    #제품소개서 다운로드
    for i in range(1,3): 
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="contents"]/div[17]/div/p['+str(i)+']/a/img'))).click()
        go_back()

    driver.get('https://www.4nb.co.kr/v2/products/ewindow.php')
    sleep(1)

#ewindow.php
    #제품소개서 다운로드
    for i in range(1,3):
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="contents"]/div[8]/div/p['+str(i)+']/a/img'))).click()
        go_back()

    driver.get('https://www.4nb.co.kr/v2/products/4nbshow.php')
    sleep(1)

#4nbshow.php
    #제품소개서 다운로드
    for i in range(1,3):
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="contents"]/div[14]/div/p['+str(i)+']/a/img'))).click()
        go_back()
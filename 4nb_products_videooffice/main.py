from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException

from time import sleep

import requests,re,unittest,HtmlTestRunner,os,sys
from bs4 import BeautifulSoup as bs

sys.path.insert(0,'c:\\selenium\\4nb\\selenium-auto-test\\4nb_common')

import footer_controller as fc
import top_nav_controller as tc
import href_tag_controller as hc
import products_category_controller as pcc

class MainTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r'C:\chromedriver.exe')
        cls.driver.implicitly_wait(30)
        cls.driver.get('https://www.4nb.co.kr/v2/products/videooffice.php')
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver,10)

    def test_footer(self):
        fc.run(self.driver,self.wait,By,EC,ActionChains,sleep)
    def test_top_nav(self):
        tc.run(self.driver,self.wait,By,EC,ActionChains,sleep,TimeoutException)
    def test_mid_contents(self):
        pcc.run(self.driver,self.wait,By,EC,ActionChains,sleep)
    def test_href_tag(self):
        hc.run(self.driver.current_url,requests,bs,re)
    
    #***not used***
    # def test_left_container(self):
    #     lc.run(self.driver,self.wait,By,EC,ActionChains,sleep,)

    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    runner = "ReportTest"
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=runner))
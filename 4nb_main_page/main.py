from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException

from time import sleep

import requests,re,unittest,HtmlTestRunner
from bs4 import BeautifulSoup as bs

import carousel_controller as ct
import footer_controller as fc
import input_controller as ic
import top_nav_controller as tc
import mid_contents_controller as mc

import href_tag_controller as hc

class MainTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r'C:\chromedriver.exe')
        cls.driver.implicitly_wait(30)
        cls.test_url_page = 'https://www.4nb.co.kr/v2/index.php'
        cls.driver.get('https://www.4nb.co.kr/v2/index.php')
        cls.driver.maximize_window()

        cls.wait = WebDriverWait(cls.driver,10)

    def test_carousel(self):
        ct.run(self.driver,self.wait,By,EC,ActionChains,sleep)
    def test_footer(self):        
        fc.run(self.driver,self.wait,By,EC,ActionChains,sleep)
    def test_input(self):
        ic.run(self.driver,self.wait,By,EC,ActionChains,sleep,Alert)
    def test_top_nav(self):
        tc.run(self.driver,self.wait,By,EC,ActionChains,sleep,TimeoutException)
    def test_mid_contents(self):
        mc.run(self.driver,self.wait,By,EC,ActionChains,sleep)
    def test_href_tag(self):
        hc.run(self.test_url_page,requests,bs,re)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    runner = "ReportTest"
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=runner))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

from time import sleep

import requests
from bs4 import BeautifulSoup as bs
import re

import carousel_controller as ct
import footer_controller as fc
import input_controller as ic
import top_nav_controller as tc
import mid_contents_controller as mc

import href_tag_controller as hc

test_url_page = 'https://www.4nb.co.kr/v2/index.php'

driver = webdriver.Chrome(r'C:\chromedriver.exe')

driver.implicitly_wait(3)

driver.get(test_url_page)
driver.maximize_window()

wait = WebDriverWait(driver,10)

ct.run(driver,wait,By,EC,ActionChains,sleep)
fc.run(driver,wait,By,EC,ActionChains,sleep)
ic.run(driver,wait,By,EC,ActionChains,sleep,Alert)
tc.run(driver,wait,By,EC,ActionChains,sleep)
mc.run(driver,wait,By,EC,ActionChains,sleep)

driver.quit()

hc.run(test_url_page,requests,bs,re)
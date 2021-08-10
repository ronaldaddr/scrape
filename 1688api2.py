from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


import time
import sys
import json
from bs4 import BeautifulSoup
import os
driver= webdriver.PhantomJS()
#url = 'https://detail.1688.com/offer/650635541901.html?spm=a260k.dacugeneral.home2019rec.6.6633436cLYnbqX&tracelog=p4p&clickid=b7ad1f4f0aff41bca346974460c0cbf1&sessionid=134b5a5d503cc164298709a41b8b3775'
url = 'https://detail.1688.com/offer/649838054631.html'

injected_javascript = (
    'document.write(JSON.stringify(iDetailConfig, undefined, 4));document.write(JSON.stringify(iDetailData, undefined, 4));'
)
print("TUNGGU")
driver.get(url)
driver.execute_script(injected_javascript)
soup = BeautifulSoup(driver.page_source, "html.parser")
print(soup)
f = open(os.getcwd() + "/649838054631.json", "w")
f.write(soup.text)
print("selesai")

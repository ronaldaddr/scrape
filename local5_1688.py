from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities
import time
import sys
import json
import chromedriver_binary  # Adds chromedriver binary to path
from bs4 import BeautifulSoup
import os


injected_javascript = (
    'const time = Date.now();'
    'const callback = arguments[0];'
    'const handleDocumentLoaded = () => {'
    '  var importirjson =[]; importirjson.push({"offerid":iDetailConfig.offerid});console.log(JSON.stringify(iDetailConfig, undefined, 4));console.log(JSON.stringify(iDetailData, undefined, 4));document.write(JSON.stringify(iDetailConfig, undefined, 4));document.write(JSON.stringify(iDetailData, undefined, 4));'
    '  callback();'
    '};'
    'if (document.readyState === "loading") {'
    '  document.addEventListener("DOMContentLoaded", handleDocumentLoaded);'
    '} else {'
    '  handleDocumentLoaded();'
    '}'
)
capabilities = DesiredCapabilities.CHROME
capabilities["loggingPrefs"] = {"performance": "ALL"}  # newer: goog:loggingPrefs
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--disable-dev-shm-usage")
#chrome_options.add_argument("--no-sandbox")
#desired_capabilities=capabilities,options=chrome_options
driver = webdriver.Chrome()
driver.implicitly_wait(10)
#driver.maximize_window()
print("TUNGGU")
html_file = "file:///" + os.getcwd() + "/1688_price2.html"
#url="https://m.1688.com/offer/646953233079.html?spm=a260k.dacugeneral.home2019rec.4.6633436cYwPvXH&resourceId=850343&udsPoolId=1026341&scm=1007.21237.114566.0&pvid=0107d36b-2a57-49bc-a296-456c2de16db7&tpp_trace=212c894216279774526528233eeddc"
#url="https://detail.1688.com/offer/620874896891.html?spm=a260k.dacugeneral.home2019rec.2.6633436cMWZYdR&resourceId=850343&udsPoolId=1026341"
#url = 'https://detail.1688.com/offer/649838054631.html?spm=a260k.dacugeneral.home2019rec.1.6633436cXYoUnX&tracelog=p4p&clickid=27318c3a60ee44e3883d7e6b8b81f4f8&sessionid=2998051d35cc0b1e3b48ac953805a838'
#url = 'https://detail.1688.com/offer/583457675025.html?spm=a260k.dacugeneral.home2019rec.86.6633436cUAUSXG&resourceId=850343&udsPoolId=1026341&scm=1007.21237.114566.0&pvid=0c171c21-3831-46ee-9256-bc267ab61166&tpp_trace=212cbb6816282789506151387e7598'
url = 'https://detail.1688.com/offer/650635541901.html?spm=a260k.dacugeneral.home2019rec.6.6633436cLYnbqX&tracelog=p4p&clickid=b7ad1f4f0aff41bca346974460c0cbf1&sessionid=134b5a5d503cc164298709a41b8b3775'
#driver.execute_script("window.open('https://1688.com/');")
#driver.switch_to.window(driver.window_handles[-1])
driver.get(url)

driver.execute_async_script(injected_javascript)
soup = BeautifulSoup(driver.page_source, "html.parser")
print(soup.text)
f = open(os.getcwd() + "/650635541901.json", "w")
f.write(soup.text)
print("selesai")

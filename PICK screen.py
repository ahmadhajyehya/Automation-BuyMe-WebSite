import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=Service("C:\\Users\\2022\Downloads\\chromedriver_win32 (3)\\chromedriver.exe"))

driver.get("https://buyme.co.il/")
time.sleep(5)
button = driver.find_element(By.LINK_TEXT, value ='חיפוש')
button.click()

driver.get("https://buyme.co.il/search")
time.sleep(3)
elm = driver.find_element(By.PARTIAL_LINK_TEXT , value="BUYME ALL")
elm.click()

driver.get("https://buyme.co.il/supplier/13438757?query=")
time.sleep(5)

driver.find_element(By.ID, "ember1347").send_keys("123")
time.sleep(2)

driver.find_element(By.ID, "ember1353").click()
time.sleep(5)


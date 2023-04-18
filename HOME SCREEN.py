import select
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("C:\\Users\\2022\Downloads\\chromedriver_win32 (3)\\chromedriver.exe"))

driver.get("https://buyme.co.il/")
time.sleep(5)

driver.find_element(By.XPATH, value="//span[@class='selected-text']").click()
time.sleep(4)

driver.find_element(By.CSS_SELECTOR, 'label[gtm=category').click()
time.sleep(4)


driver.find_element(By.XPATH, value="//span[@title='אזור']").click()
time.sleep(4)



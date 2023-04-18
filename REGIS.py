from selenium.webdriver.common.by import By
import time
from time import sleep
import warnings
from webdriver_manager import drivers
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with
from selenium import webdriver



driver = webdriver.Chrome(service=Service("C:\\Users\\2022\Downloads\\chromedriver_win32 (3)\\chromedriver.exe"))
driver.get('https://buyme.co.il/?modal=login')

driver.find_element(By.XPATH, value="//span[@class='text-link theme']").click()
time.sleep(2)

driver.find_element(By.XPATH, value="//input[@placeholder='שם פרטי']").send_keys("ahmad")
time.sleep(2)

driver.find_element(By.XPATH, value="//input[@placeholder='מייל']").send_keys("barcelona135798@gmail.com")
time.sleep(2)

driver.find_element(By.XPATH, value="//input[@placeholder='סיסמה']").send_keys("Ahmad.11.22")
time.sleep(2)

driver.find_element(By.XPATH, value="//input[@placeholder='אימות סיסמה']").send_keys("Ahmad.11.22")
time.sleep(2)

driver.find_element(By.XPATH, value="//span[@class='bm-body-2 label']").click()
time.sleep(2)

driver.find_element(By.XPATH, value="//div[@class='ember-view bm-checkbox']").click()
time.sleep(2)

driver.find_element(By.XPATH, value="//button[@gtm='הרשמה ל-BUYME']").click()
time.sleep(3)



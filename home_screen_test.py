from selenium.webdriver.common.by import By
from base_page import BasePage
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver





class HomeScreen(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)


    def test_home_screen(self):
        driver = webdriver.Chrome(service=Service("C:\\Users\\2022\Downloads\\chromedriver_win32 (3)\\chromedriver.exe"))
        driver.get("https://buyme.co.il/")
        time.sleep(2)
        driver.find_element(By.XPATH, value="//span[@class='selected-text']").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, 'label[gtm=category').click()
        time.sleep(2)
        driver.find_element(By.XPATH, value="//span[@title='אזור']").click()
        time.sleep(2)



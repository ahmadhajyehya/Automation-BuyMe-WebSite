import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base_page import BasePage


class SenderReceiver(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)


    def Sender_Receiver(self):

        driver = webdriver.Chrome(service=Service("C:\\Users\\2022\Downloads\\chromedriver_win32 (3)\\chromedriver.exe"))
        driver.get("https://buyme.co.il/supplier/13438757?query=")
        driver.implicitly_wait(5)


        driver.find_element(By.ID, "ember1347").send_keys("123")
        time.sleep(2)
        driver.find_element(By.ID, "ember1353").click()
        time.sleep(2)

        driver.find_element(By.ID, "friendName").send_keys("AAA123")
        time.sleep(2)

        driver.find_element(By.XPATH, value="//span[@class='selected-text']").click()
        time.sleep(4)

        driver.find_element(By.XPATH, value="//span[@class='selected-text']").click()

        driver.find_element(By.XPATH,"//textarea[@placeholder='מזל טוב, תודה רבה או פשוט מלא אהבה? כאן כותבים מילים טובות ואיחולים שמחים']").send_keys("ffeeed12edJJe")
        time.sleep(2)

        driver.find_element(By.XPATH, value ='/html/body/div[4]/div/div/div[3]/div/div/div[1]/form/div[2]/div[5]/div[2]/div[1]/label/input').send_keys("C:\\Users\\2022\\Documents\\ahmad123.png")
        time.sleep(2)

        driver.find_element(By.XPATH, value="//span[@class='label']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, value="//input[@placeholder='שם שולח המתנה']").send_keys("ahmad.s.123")
        time.sleep(2)


        driver.find_element(By.CLASS_NAME, "toggle-icon").click()
        time.sleep(2)

        driver.find_element(By.XPATH,value="//input[@placeholder='נייד מקבל/ת המתנה']").send_keys("0524407037")
        time.sleep(2)

        driver.find_element(By.XPATH,value="//input[@placeholder='מספר נייד']").send_keys("0524406039")
        time.sleep(2)


        driver.find_element(By.CSS_SELECTOR,'svg[gtm=method-email').click()
        time.sleep(2)

        driver.find_element(By.XPATH,value="//input[@placeholder='מייל מקבל/ת המתנה']").send_keys("ahmad12345@gmail.com")
        time.sleep(2)

        driver.find_element(By.XPATH, value="//button[@gtm='המשך לתשלום']").click()
        time.sleep(3)




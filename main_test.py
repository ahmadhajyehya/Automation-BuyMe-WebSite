from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.chrome.options import Options
from Registrationscreen_test import registration
from home_screen_test import HomeScreen
from pick_business_test import PickBusiness
from sender_and_receiver import SenderReceiver
import allure


class TestBuyMeWebsite(TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.Registraionscreen_test = registration(self)
        self.driver = None

    def setUp(self) -> None:

        driver = webdriver.Chrome(service=Service("C:\\Users\\2022\Downloads\\chromedriver_win32 (3)\\chromedriver.exe"))
        driver.get('https://buyme.co.il/?modal=login')
        self.Registrationscreen_test = registration(self.driver)
        self.home_screen = HomeScreen(self.driver)
        self.pick_business = PickBusiness(self.driver)
        self.sender_and_receiver = SenderReceiver(self.driver)


    def test_1_registration(self):
        self.Registraionscreen_test.test_registration()
    def test_2_home_screen(self):
        self.home_screen.test_home_screen()
    def test_3_pick_business(self):
        self.pick_business.test_pick_business()
    def test_4_Sender_information(self):
        self.sender_and_receiver.Sender_Receiver()

    def tearDown(self) -> None:
        self.driver.quit()
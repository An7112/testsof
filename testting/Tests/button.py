
from selenium import webdriver
import unittest
import time
from PageObjects.buttonclick import Button
from webdriver_manager.chrome import ChromeDriverManager
button_xpath ="/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer"
class InputPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_input(self):
        self.driver.get("https://www.youtube.com/")
        button = Button(self.driver)
        button.test_button_text1()
        time.sleep(2)
        button.test_button_text2()
        time.sleep(2)
        button.test_button_text3()
        time.sleep(2)
        button.test_button_text4()
        time.sleep(2)
        button.test_button_text5()
        time.sleep(2)
        button.test_button_text6()
        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
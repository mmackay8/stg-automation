import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class slingSearch (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
    def tearDown(self):
        self.driver.close()
    def test_challenge2(self):
        self.driver.get("https://sling.com")
        channels = self.driver.find_elements_by_xpath('//*[@id="channelList"]//img')
        for i in channels:
            print(i.get_attribute('title'))
        print(len(channels))




if __name__ == '__main__':
    unittest.main()
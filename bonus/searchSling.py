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
        self.driver.get("https://help.sling.com")
        self.assertIn("Help Center", self.driver.title)
        search = self.driver.find_element_by_xpath('//*[@id="support-search-input"]')
        search.click()
        search.send_keys("roku") #FIXME here
        search.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul')))
        results = self.driver.find_elements_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul/section')
        print(len(results))




if __name__ == '__main__':
    unittest.main()
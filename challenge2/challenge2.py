import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Challenge2 (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
    def tearDown(self):
        self.driver.close()
    def test_challenge2(self):
        self.driver.get("https://copart.com")
        self.assertIn("Copart", self.driver.title)
        search = self.driver.find_element_by_id("input-search")
        search.send_keys("exotics")
        search.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="serverSideDataTable"]/tbody/tr[1]/td[5]/span')))




if __name__ == '__main__':
    unittest.main()
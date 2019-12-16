import unittest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

class Challenge3 (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        self.driver.get("https://copart.com")
        self.assertIn("Copart", self.driver.title)
        pop = self.driver.find_elements_by_xpath('//*[@id="tabTrending"]/div[1]/div[2]/div/ul/li/a')
        assert pop
        print(pop)
        assert len(pop) > 0
        myDict = {}
        for item in pop:
            name = item.text
            href = item.get_attribute("href")
            myDict[name] = href

        for key, href in myDict.items():
            self.driver.get(href)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mainBody"]/div[1]/div/div[1]/div[1]/div/div[2]/div[3]/h1/span[2]')))

            searchedFor =self.driver.find_element_by_xpath('//*[@id="mainBody"]/div[1]/div/div[1]/div[1]/div/div[2]/div[3]/h1/span[2]').text
            self.assertTrue(key.lower()+"is not in "+searchedFor, key.lower() in searchedFor)








if __name__ == '__main__':
    unittest.main()
import unittest

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
        for item in pop:
            name = item.text
            href = item.get_attribute("href")
            print("{} - {}".format(name, href))


if __name__ == '__main__':
    unittest.main()
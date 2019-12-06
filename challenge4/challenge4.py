import unittest
from fib import Fib
from convertNumToString import ConvertNumToString
from selenium import webdriver
class Challenge4 (unittest.TestCase):



    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        self.f = Fib()
        self.s = ConvertNumToString()

    def tearDown(self):
        self.driver.close()

    def test_challenge4(self):
        print(self.s.number_to_string(self.f.fib(30)))



if __name__ == '__main__':
    unittest.main()

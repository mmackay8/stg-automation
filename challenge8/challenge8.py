import unittest
import requests
import json
#from urllib2 import Request, urlopen
#from urllib import urlopen, request
from selenium import webdriver




class Challenge3 (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")


    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        log = open("log.txt", "w")
        self.driver.get("https://copart.com")
        items = ["toyota camry", "toyota corolla le", "nissan skyline", "nissan altima", "ford mustang", "suburban", "ford f150", "ferrari", "porsche", "tesla"]
        for item in items:
            url = "https://www.copart.com/public/lots/search"
            header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
            data = {"query": item}
            res = requests.post(url, headers=header, data=data)
            response = json.loads(res.text)
            log.write("{} {}\n".format(item, response['data']['results']['totalElements']))
        log.close()



if __name__ == '__main__':
    unittest.main()
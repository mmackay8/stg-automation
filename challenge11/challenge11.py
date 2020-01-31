import requests
from bs4 import BeautifulSoup
import unittest
from selenium import webdriver
from link_finder import LinkFinder

def addToQueue(url, queue, visited):
        if url.startswith("/."):
            url = url.replace(".", "https://www.copart.com")
            if(url not in visited):
                queue.add(url)
        elif url.startswith("/"):
            url = "https://www.copart.com" + url
            if(url not in visited):
                queue.add(url)
        elif "copart.com" in url and url not in visited:
            queue.add(url)


class Challenge3 (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
    def tearDown(self):
        self.driver.close()

    def test_challenge11(self):
        start_url = "https://copart.com"
        toVisit = set()
        visited = set()
        toVisit.add(start_url)
        while (len(toVisit) > 0):
            next_url = toVisit.pop()
            print(next_url)
            print(len(toVisit))
            print(toVisit)
            print(visited)
            self.driver.get(next_url)
            source = self.driver.page_source
            bs = BeautifulSoup(source, features="html.parser")
            visited.add(next_url)
            for link in bs.findAll('a', href=True):
                href = link.get('href')
                addToQueue(href, toVisit, visited)

        out = open("log.txt", 'w')
        for link in visited:
            out.write(link+"\n")
        out.close()



if __name__ == '__main__':
    unittest.main()



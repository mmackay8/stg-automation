import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Challenge5 (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def switch(self, case):
        if case == 'REAR END': return 'REAR END'
        elif case == 'FRONT END': return'FRONT END'
        elif case == 'MINOR DENT/SCRATCHES': return'MINOR DENT/SCRATCHES'
        elif case == 'UNDERCARRIAGE': return'UNDERCARRIAGE'
        else: return'MISC'


    def test_challenge5(self):
        self.driver.get("https://copart.com")
        self.assertIn("Copart", self.driver.title)
        search = self.driver.find_element_by_id("input-search")
        search.send_keys("porsche")
        search.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="serverSideDataTable_length"]/label/select')))

        entriesShown = self.driver.find_element_by_name("serverSideDataTable_length")
        select = Select(entriesShown)
        select.select_by_visible_text("100")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="serverSideDataTable"]/tbody/tr[100]')))
        tableId = self.driver.find_element_by_id("serverSideDataTable")
        modelCols = self.driver.find_elements_by_xpath('//*[@id="serverSideDataTable"]/tbody/tr/td[6]/span[text()]')
        models = {}
        damageCols = self.driver.find_elements_by_xpath('//*[@id="serverSideDataTable"]/tbody/tr/td[12]/span[text()]')
        damage = {}
        for item in modelCols:
            if item.text in models.keys():
                models[item.text] = int(models[item.text])+1
            else:
                models[item.text] = 1
        print(models)

        for item in damageCols:
            damageType = self.switch(item.text)
            if damageType in damage.keys():
                damage[damageType] = int(damage[damageType]) + 1
            else:
                damage[damageType] = 1
        print(damage)

        #//*[@id="serverSideDataTable"]/tbody/tr[1]/td[12]/span
        # print(tableCols.text)
        # cols = tableId.find_elements(By.TAG_NAME, "tr")
        # print(cols)
        # for item in cols:
        #     print(item.text)
        # #cols = tableId.find_elements(By.TAG_NAME, "td")[1].text  # get all of the rows in the table
        # #print(cols)
        # #dict = {}
        # #for item in cols:
        #  #   print(item)
        #   #  print(item.text)
        #    # if item.text in dict.keys():
        #     #    dict[item.text] = dict[item]+1
        #   #  else:
        #    #     dict[item.text] = 1
        # print(dict)

if __name__ == '__main__':
    unittest.main()
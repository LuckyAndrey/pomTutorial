import unittest
from selenium import webdriver
from Pages.Interactions.Selectable import Selectable_default, Selectable_Serialaze


class Default_Select(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


    # def test_quantity_items(self):
    #     driver = self.driver
        # driver.get('http://demo.automationtesting.in/Selectable.html')
        #
        # page = Selectable_default(driver)
        # page.itemsis_displayed()
        # page.itemsis_enabled()
        # page.select_one()

    def test_Serialer(self):
        driver = self.driver
        driver.get('http://demo.automationtesting.in/Selectable.html')
        driver.find_element_by_xpath('//a[@href="#Serialize"]').click()

        page = Selectable_Serialaze(driver)
        page.select_serial()

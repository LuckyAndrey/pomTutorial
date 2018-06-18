import unittest

from selenium import webdriver

from Pages.Widgets import Accordion_Wigets, Locators


class Test_wedgets(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):

        cls.driver.close()
        cls.driver.quit()


    def test_collaps1(self):
        driver = self.driver
        driver.get(Locators.url)
        print(driver.title)
        print(driver.current_url)
        page = Accordion_Wigets(driver)
        # driver.find_element_by_xpath().text
        page.clickOnCollapsibleGroup1()
        page.clickOnCollapsibleGroup2()
        page.clickOnCollapsibleGroup3()
        page.clickOnCollapsibleGroup4()
        # page.getText()


if __name__ == '__main__':
    unittest.main()
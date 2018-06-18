import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException

from Pages.WebTable_Page import WebTable_Page, LocatorWebTable


class TestWebTable(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        print('exeptions {}, alerts {} '.format(self.verificationErrors, self.accept_next_alert))

    def etest_verify_selectedItemsEqualQuantityRows1(self):
        driver = self.driver
        driver.get(LocatorWebTable.url)
        page = WebTable_Page(driver)
        d = page.change_items_per_page(10)
        print(' selected 10 items, shown {} items'.format(d))
        self.assertEqual(d, 10)
        driver.implicitly_wait(5)

    def etest_verify_selectedItemsEqualQuantityRows2(self):
        driver = self.driver
        driver.get(LocatorWebTable.url)
        page = WebTable_Page(driver)
        d = page.change_items_per_page(20)
        print(' selected 20 items, shown {} items'.format(d))
        self.assertEqual(d, 20)
        driver.implicitly_wait(5)


    def etest_verify_selectedItemsEqualQuantityRows3(self):
        driver = self.driver
        driver.get(LocatorWebTable.url)
        page = WebTable_Page(driver)
        d = page.change_items_per_page(30)
        print(' selected 30 items, shown {} items'.format(d))
        self.assertEqual(d, 30)
        driver.implicitly_wait(5)

    def etest_pagination(self):
        driver = self.driver
        driver.get(LocatorWebTable.url)
        page = WebTable_Page(driver)
        page.paggination_last()
        time.sleep(3)
        page.paggination_first()
        time.sleep(3)


    def test_edit_button(self):
        driver = self.driver
        driver.get(LocatorWebTable.url)
        page = WebTable_Page(driver)
        page.click_button_edit()
        net = driver.get_network_conditions()
        print(net)
        time.sleep(5)
        # print(driver.find_element_by_xpath(
        #     '//div[@class="ui-grid-cell-contents ng-binding ng-scope ui-grid-cell-contents-hidden"]').is_enabled())
        # driver.find_element_by_css_selector().id

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True


if __name__ == '__main__':
    unittest.main()
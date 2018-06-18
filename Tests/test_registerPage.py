# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

from Pages.WebTable_Page import WebTable_Page, LocatorWebTable
from Pages.registerPage import RegisterPage


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver

        regPage = RegisterPage(driver)
        url = LocatorWebTable.url
        print(url)
        driver.get(url)
        # driver.get(regPage.url())

        # links = regPage.get_links('a', 'href')
        # print(links)
        # regPage.checkLinks(links)

        # regPage.type_user_name('Ivan', 'Morkovkin')
        # regPage.type_user_address_phone_email('32 lenina', 456-456-4555, "lkkl@sd.ru")
        # regPage.select_countries('Algeria')
        # regPage.select_country('Hong Kong')
        # regPage.select_Male_radioButton()
        # regPage.select_Female_radioButton()
        # regPage.click_checkboxes()
        # regPage.set_languages()
        # assert regPage.count_languages() == 41
        # print(regPage.verify_now_many_languages_selected())

        # regPage.skills()
        # regPage.set_skills()



# ----------------------------------------------------
#         driver.get(WebTable_Page.url())
        s = WebTable_Page(driver)

        s.count_rows()

# --------------------------------------------------------
        # time.sleep(5)

        # driver.find_element_by_id("Skills").click()
        # Select(driver.find_element_by_id("Skills")).select_by_visible_text("Analytics")
        # driver.find_element_by_id("Skills").click()

        # driver.find_element_by_id("countries").click()
        # driver.find_element_by_id("countries").click()
        # driver.find_element_by_id("select2-country-container").click()

        # driver.find_element_by_id("yearbox").click()
        # Select(driver.find_element_by_id("yearbox")).select_by_visible_text("1929")
        # driver.find_element_by_id("yearbox").click()
        # driver.find_element_by_xpath("(//select[@type='text'])[4]").click()
        # Select(driver.find_element_by_xpath("(//select[@type='text'])[4]")).select_by_visible_text("7")
        # driver.find_element_by_xpath("(//select[@type='text'])[4]").click()
        # driver.find_element_by_id("daybox").click()
        # Select(driver.find_element_by_id("daybox")).select_by_value() .select_by_visible_text("18")
        # driver.find_element_by_id("daybox").click()

        # driver.find_element_by_id("firstpassword").click()
        # driver.find_element_by_id("firstpassword").clear()
        # driver.find_element_by_id("firstpassword").send_keys("123")

        # driver.find_element_by_id("secondpassword").click()
        # driver.find_element_by_id("secondpassword").clear()
        # driver.find_element_by_id("secondpassword").send_keys("123")

        # driver.find_element_by_id("imagesrc").click()
        # driver.find_element_by_id("imagesrc").clear()
        # driver.find_element_by_id("imagesrc").send_keys("C:\\fakepath\\00J0J_fYMlDGzlMiN_600x450.jpg")

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

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        print('exeptions {}, alerts {} '.format(self.verificationErrors, self.accept_next_alert))


if __name__ == "__main__":
    unittest.main()

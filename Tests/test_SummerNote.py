from selenium import webdriver
import unittest
from Pages.WYCIWYG.SummerNote import SummerNote, Locators
from utils_tools.enviroment import EnvironmentSetup

# class Summer(EnvironmentSetup):
class Summer(unittest.TestCase):
    #
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_resizeUp(self):

        driver = self.driver
        driver.get(Locators.url)

        page = SummerNote(driver)
        page.resizeUp()

    def test_select_All(self):

        driver = self.driver
        driver.get(Locators.url)

        page = SummerNote(driver)
        page.select_All()

    def test_write_line(self):

        driver = self.driver
        driver.get(Locators.url)

        page = SummerNote(driver)
        page.delete_All()
        page.write_line()

    def test_click_all_buttons(self):

        driver = self.driver
        driver.get(Locators.url)

        page = SummerNote(driver)
        page.click_all_buttons()

    def test_make_table(self):

        driver = self.driver
        driver.get(Locators.url)

        page = SummerNote(driver)
        page.delete_All()
        page.make_table(5, 5)

    def test_make_bold(self):

        driver = self.driver
        driver.get(Locators.url)

        page = SummerNote(driver)
        page.select_All()

        page.click_button(Locators.bold_button)
        self.assertTrue(page.is_text_formated(Locators.is_bold))

    def test_make_underline(self):
        driver = self.driver
        driver.get(Locators.url)

        page = SummerNote(driver)
        page.select_All()
        page.click_button(Locators.underLine_button)
        self.assertTrue(page.is_text_formated(Locators.is_underLine))
        # print(page.is_text_formated(Locators.is_underLine))

    def test_make_bold_underline(self):
        driver = self.driver
        driver.get(Locators.url)

        page = SummerNote(driver)
        page.select_All()
        page.click_button(Locators.bold_button)
        page.click_button(Locators.underLine_button)

        self.assertTrue(page.is_text_formated(Locators.is_bold_underline))

    def test_make_underline_bold(self):
        driver = self.driver
        driver.get(Locators.url)

        page = SummerNote(driver)
        page.select_All()
        page.click_button(Locators.underLine_button)
        page.click_button(Locators.bold_button)

        self.assertTrue(page.is_text_formated(Locators.is_underline_bold))
        # print(page.is_text_bold_underlined())


        # page.make_unordered_list()
        # page.make_ordered_list()
        # page.make_paragraph()
        # page.make_table(5, 5)
        # page.make_link('text', 'url')
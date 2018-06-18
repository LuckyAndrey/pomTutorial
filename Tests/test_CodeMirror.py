from selenium import webdriver
from unittest import TestCase
import time
from utils_tools.enviroment import EnvironmentSetup
from Pages.WYCIWYG.CodeMirrorPage import CodeMirror
from utils_tools.check_links import BrokenLink

class Code(TestCase):
# class Code(EnvironmentSetup):
    # driver = self.driver

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_links(self):
        driver = self.driver
        driver.get('http://demo.automationtesting.in/WebTable.html')
        page = BrokenLink(driver)
        page.broken_links()

    # def test_empty_field(self):
    #     driver = self.driver
    #     driver.get(CodeMirror.Locator.url)
    #     page = CodeMirror(driver)
    #     page.lineNumber()
    #
    #
    # def test_checkHowManyLines(self):
    #     driver = self.driver
    #     driver.get(CodeMirror.Locator.url)
    #     page = CodeMirror(driver)
    #     page.lineNumber()
    #     lines = page.verifyTextFieldEmpty()
    #     print(lines)
    #     # self.assertEqual(lines, 1)
    #     time.sleep(5)
    #
    # def test_type_text(self):
    #
    #     driver = self.driver
    #     driver.get(CodeMirror.Locator.url)
    #     page = CodeMirror(driver)
    #     page.enterLines(2, 'Hello ')

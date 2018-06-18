import time
import unittest

from selenium import webdriver

from Pages.Interactions.InteractionDynamic import Locators, DynamicDrop


class DragAndDropTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get(Locators.url)
        # driver = self.driver
        self.page = DynamicDrop(self.driver)
        print("title is ", self.driver.title, 'URL = ', self.driver.current_url)


    def tearDown(self):
        print("Exit")
        time.sleep(5)
        self.driver.close()
        self.driver.quit()

    def test_items_are(self):
        print('total items are = ',len(self.page.verify_drag_items_are()))
        print('trying drag and drop')
        self.page.drag_element()
        time.sleep(6)
        self.page.verify_that_element_droped()
        # self.driver.find_element_by_xpath().get_attribute()

    # def test_all_items_moved(self):
    #
        # driver = self.driver
        # page = InteractionDragAndDropStatic(driver)
        # self.page.chose_menu_item('Dynamic ')


import unittest

from selenium import webdriver

from Pages.Interactions.Interactions_Page import Locators, StaticDrop, DynamicDrop


class DragAndDropTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get(Locators.url)
        # driver = self.driver
        self.page = StaticDrop(self.driver)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_items_are(self):
        page = DynamicDrop(self.driver)
        page.ch
        page.verify_drag_items_are()

    def test_all_items_moved(self):

        # driver = self.driver
        # page = InteractionDragAndDropStatic(driver)
        self.page.chose_menu_item('Static')


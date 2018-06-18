from random import randint
from selenium.webdriver.common.action_chains import ActionChains


class DynamicDrop(object):
    def __init__(self, driver):
        self.driver = driver

    def chose_menu_item(self, nameOfmenu):
        self.driver.get("http://demo.automationtesting.in/Static.html")
        self.driver.find_element_by_link_text("Interactions").click()
        self.driver.find_element_by_link_text("Drag and Drop").click()
        self.driver.find_element_by_link_text(nameOfmenu).click()
        # self.driver.find_element_by_link_text("Static").click()

    def hightlight_element(self, element):
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                                   "color:tomato; border:3px solid yellow;")

    def verify_drag_items_are(self):
        return self.driver.find_elements_by_xpath(Locators.drag_items)

    def check_max_size_of_dynamic_frame(self):
        size = self.driver.find_element_by_xpath(Locators.target)

    def drop_randomn_img(self):
        elements = self.driver.find_elements_by_xpath(Locators.drag_items)
        return elements[randint(0, len(elements))]

    def drag_element(self):
        self.driver.switch_to.frame(0)
        # target = self.driver.find_element_by_xpath(Locators.target)
        # color = self.driver.find_element_by_xpath(Locators.target).get_attribute("style")
        # print('color  ', color)
        element = self.driver.find_elements_by_xpath(Locators.droppedItems)[1]
        self.hightlight_element(element)
        # target = self.driver.find_element_by_id("msg")
        target = self.driver.find_element_by_xpath(Locators.target)
        self.hightlight_element(target)

        print('element', element)
        print('target', target)
        ActionChains(self.driver).drag_and_drop(element, target).perform()
        self.verify_that_element_droped()


    def verify_that_element_droped(self):
        moved_items = len(self.driver.find_elements_by_xpath(Locators.droppedItems))
        print('Moved {} elements'.format(moved_items))



class Locators:
    url = "http://demo.automationtesting.in/Dynamic.html"
    menu_interaction = '//a[@href="Interactions.html"]'
    sub_menu_drag_and_drop = ''

    # Dynamic ---------------------------
    nameOfMenu = 'Dynamic '
    target = '//p[@id="msg"]'
    droppedItems = '//div[@id="droparea"]/p/div'
    dragarea = '//div[@id="dragarea"]/p/div'
    # dragarea = '//div[@id="dragarea"]/p/div'
    drag_items = '//div[@id="dragarea"]/div'


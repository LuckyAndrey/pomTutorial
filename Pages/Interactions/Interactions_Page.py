from random import randint

class StaticDrop(object):

    def __init__(self, driver):
        self.driver = driver

    def chose_menu_item(self, nameOfmenu):
        self.driver.get("http://demo.automationtesting.in/Static.html")
        self.driver.find_element_by_link_text("Interactions").click()
        self.driver.find_element_by_link_text("Drag and Drop").click()
        self.driver.find_element_by_link_text(nameOfmenu).click()
        # self.driver.find_element_by_link_text("Static").click()


    def verify_drag_items_are(self):
        return self.driver.find_element_by_xpath(Locators.drag_items)


    def static(self):

        pass



class DynamicDrop(object):

    def __init__(self, driver):
        self.driver = driver

    def verify_drag_items_are(self):
        return self.driver.find_element_by_xpath(Locators.drag_items)


    def check_max_size_of_dynamic_frame(self):
        size = self.driver.find_element_by_xpath(Locators.droparea)

    def drop_randomn_img(self):
        elements = self.driver.find_element_by_xpath(Locators.drag_items)
        return elements[randint(0,len(elements))]



class Locators:

    url = "http://demo.automationtesting.in/Static.html"
    menu_interaction = '//a[@href="Interactions.html"]'
    sub_menu_drag_and_drop = ''

    # Dynamic ---------------------------
    nameOfMenu = 'Dynamic '
    droparea ='//div[@id="droparea"]/p/div'
    dragarea ='//div[@id="dragarea"]/p/div'
    drag_items = '//div[@id="dragarea"]/div'


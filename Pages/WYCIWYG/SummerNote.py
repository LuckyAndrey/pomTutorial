import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class SummerNote(object):

    def __init__(self, driver):
        self.driver = driver

    # work
    def resizeUp(self):
        anchor = self.driver.find_element_by_xpath(Locators.resizeAnchor)
        anchor_line = self.driver.find_element_by_xpath('//div[@class="note-resizebar"]')
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", anchor_line,
                                   "color:green; background-color: tomato;")
        action = ActionChains(self.driver)
        action.move_to_element(anchor)
        action.click_and_hold(anchor)
        action.move_by_offset(0, 300)
        action.release()
        action.perform()
        time.sleep(5)

    def write_line(self, numsLines = 5, text="Hello World!"):
        xpath = '//div[@class="note-editable panel-body"]/p'
        self.select_All()
        for i in range(1,numsLines):
            line = self.driver.find_element_by_xpath(xpath + '[' + str(i) + ']')
            action = ActionChains(self.driver)
            action.move_to_element(line)
            action.click()
            # action.send_keys(Keys.CONTROL+ u'\u0041').perform()
            # action.send_keys(Keys.DELETE)
            # action.perform()
            # time.sleep(1)
            action.send_keys(text)
            action.send_keys(u'\ue007')
            action.perform()

    def select_chars(self,ln, start, end):
        line = self.driver.find_element_by_xpath('//div[@class="note-editable panel-body"]/p' + '[' + str(ln) + ']').text

    def select_All(self):
        element = self.driver.find_element_by_xpath(Locators.textField)
        txt = element.text
        # self.highlightElement(element)
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()
        action.send_keys(Keys.CONTROL + '\u0061').perform()

    def delete_All(self):
        element = self.driver.find_element_by_xpath(Locators.textField)
        txt = element.text
        self.highlightElement(element)
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()
        action.send_keys(Keys.CONTROL + '\u0061')
        action.send_keys(Keys.DELETE)
        action.perform()

    def click_all_buttons(self):
        buttons = [Locators.bold_button, Locators.underLine_button]
        action = ActionChains(self.driver)
        for i in buttons:
            btn = self.driver.find_element_by_xpath(i)
            action.move_to_element(btn)
            # action.click()
            action.perform()
            self.select_All()
            time.sleep(3)
            action.click()
            action.perform()
            time.sleep(3)

    def highlightElement(self,elem):
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", elem,
                              "color:green; background-color: tomato;")

    def make_table(self, row=3, column=5):

        button = '//div[@class="note-btn-group btn-group note-table"]' \
                 '//button[@class="note-btn btn btn-default btn-sm dropdown-toggle"] '
        btn = self.driver.find_element_by_xpath(button)
        self.highlightElement(btn)
        btn.click()
        e = self.driver.find_element_by_xpath('//div[@class="note-dimension-picker"]'
                                         '/div[@class="note-dimension-picker-highlighted"]')
        self.highlightElement(e)
        act = ActionChains(self.driver)
        act.move_to_element(e)
        act.move_by_offset(160, 160)
        act.click()
        act.perform()
        time.sleep(5)

    def click_button(self, button):
        # element = self.driver.find_element_by_xpath('//div[@class="note-editable panel-body"]/p')
        # txt = element.text
        # self.highlightElement(element)
        # action = ActionChains(self.driver)
        # action.move_to_element(element).click().perform()
        # action.send_keys(Keys.CONTROL + '\u0061').perform()
        self.highlightElement(self.driver.find_element_by_xpath(button))
        # self.select_All()

        action2 = ActionChains(self.driver)
        btn = self.driver.find_element_by_xpath(button)
        action2.move_to_element(btn)
        action2.click().perform()
        time.sleep(1)

        # return  self.is_text_formated()

    def is_text_formated(self, element):
        try:
            self.driver.find_element_by_xpath(element)
            # print(' Element found ')
            return True
        except:
            print(' Element not found ')
            return  False


class Locators:
    url = 'http://demo.automationtesting.in/SummerNote.html'
    resizeAnchor = '//div[@class="note-icon-bar"]'
    string = '//div[@class="note-editable panel-body"]/p'
    textField = '//div[@class="note-editable panel-body"]/p'
#     buttons bold
    bold_button = '//button[@class="note-btn btn btn-default btn-sm note-btn-bold"]'
    is_bold = '//div[@class="note-editable panel-body"]/p/b'

    underLine_button = '//button[@class="note-btn btn btn-default btn-sm note-btn-underline"]'
    is_underLine = '//div[@class="note-editable panel-body"]/p/u'

    is_bold_underline = '//div[@class="note-editable panel-body"]/p/b/u'
    is_underline_bold = '//div[@class="note-editable panel-body"]/p/u/b'

    unordereed = '//button[@class="note-btn btn btn-default btn-sm"]'
    table = '//button[@class="note-btn btn btn-default btn-sm dropdown-toggle"]'


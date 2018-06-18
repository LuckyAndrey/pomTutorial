from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains



class WebTable_Page(object):

    def __init__(self, driver):
        self.driver = driver

    def url(self):
        return "http://demo.automationtesting.in/WebTable.html"

    def count_rows(self):
        print(' selected 30 items, shown {} items'.format(self.change_items_per_page(30)))
        print(' selected 20 items, shown {} items'.format(self.change_items_per_page(20)))
        print(' selected 10 items, shown {} items'.format(self.change_items_per_page(10)))

    def change_items_per_page(self, items):
        data = []
        Select(self.driver.find_element_by_xpath("//select")).select_by_visible_text(str(items))
        for i in self.driver.find_elements_by_xpath('//div[@class="ui-grid-row ng-scope"]'):
            data.append(i)
        # print('there are {} rows'.format(len(data)))
        return len(data)

    def paggination_last(self):
        self.driver.find_element_by_xpath(LocatorWebTable.paggination_last).click()
        actual = self.driver.find_element_by_xpath(LocatorWebTable.page_number)
        print(actual)

    def paggination_first(self):
        self.driver.find_element_by_xpath(LocatorWebTable.paggination_first).click()
        actual = self.driver.find_element_by_xpath(LocatorWebTable.page_number)
        print(actual)

    def click_button_edit(self):
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait
        # a  = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.driver.find_element_by_xpath('//div[@class="ui-grid-cell-contents ng-binding ng-scope"][1]')))
        # print(a)
        status_before = self.driver.find_element_by_xpath('//div[@class="ui-grid-cell-contents ng-binding ng-scope"][1]').text
        self.driver.find_element_by_xpath('//div[@class="ui-grid-cell-contents ng-binding ng-scope"][1]').send_keys('NONE')

        status_after = self.driver.find_element_by_xpath('//div[@class="ui-grid-cell-contents ng-binding ng-scope"][1]').text
        print(status_after == status_before)

        # status_before = status_before.get_property() # = 'Read only'
        print('status_before  ', status_before)
        btn = self.driver.find_element_by_xpath(LocatorWebTable.button_edit)
        action = ActionChains(self.driver)
        action.double_click(btn).perform()
        # status_after = self.driver.find_element_by_css_selector(
        #     '#\\31 527883378993-0-uiGrid-0005-cell > div.ui-grid-cell-contents.ng-binding.ng-scope.ui-grid-cell-contents-hidden').is_enabled()
        # status_after = 'Read only'
        # print('status_after  ', status_after)


class LocatorWebTable:
    url = "http://demo.automationtesting.in/WebTable.html"
    rows = '//div[@class="ui-grid-canvas"]/div'
    itemsPerPage = (By.XPATH, '//*[@class="ng-valid ng-dirty ng-valid-parse ng-touched"]/option')
    paggination_last = '//button[@class="ui-grid-pager-last"]'
    paggination_first = '//button[@class="ui-grid-pager-first"]'
    page_number = '//input[@class="ui-grid-pager-control-input ng-pristine ng-valid ng-valid-min ng-valid-max ng-valid-required ng-touched"]'
    button_edit = '//div[@class="avddbl"]/button[@class="btn btn-xs btn-custom"]'
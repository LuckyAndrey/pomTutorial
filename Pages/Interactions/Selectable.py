import time


class Selectable_default(object):

    def __init__(self, driver):
        self.driver = driver

    def get_items(self):
        items = self.driver.find_elements_by_xpath('//ul[@class="deaultFunc"]/li')
        print('items ', len(items))
        return items

    def selected(self):
        for i in self.get_items():
            print('is_selected ? ',i.is_selected())

    def itemsis_enabled(self):
        for i in self.get_items():
            print('is_enabled ? ',i.is_enabled())

    def itemsis_displayed(self):
        for i in self.get_items():
            print('is_displayed ? ',i.is_displayed())


    def select_one(self):
        for i in self.get_items():
            i.click()
            time.sleep(2)


class Selectable_Serialaze(object):

    def __init__(self, driver):
        self.driver = driver

    def get_items(self):
        items = self.driver.find_elements_by_xpath('//ul[@class="SerializeFunc"]/li')
        print('items ', len(items))
        return items

    def selected(self):
        for i in self.get_items():
            print('is_selected ? ', i.is_selected())

    def itemsis_enabled(self):
        for i in self.get_items():
            print('is_enabled ? ', i.is_enabled())

    def itemsis_displayed(self):
        for i in self.get_items():
            print('is_displayed ? ', i.is_displayed())

    def select_serial(self):
        for i in self.get_items():
            i.click()
            description = self.driver.find_element_by_xpath('//*[@id="result"]').text
            print(' Selected {} - showed {}'.format(i.text, description))
            time.sleep(2)



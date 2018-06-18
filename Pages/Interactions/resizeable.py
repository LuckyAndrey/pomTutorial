from  selenium.webdriver.common.action_chains import ActionChains
class Resize(object):

    def __init__(self, driver):
        self.driver = driver

    def findPoint(self):
        return  self.driver.find_element_by_xpath('//*[@id="resizable"]/div[3]')

    def increase_size(self):
        point = self.findPoint()
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", point,
                              "color:green; background-color: tomato;")
        box = self.driver.find_element_by_xpath('/html/body/section/div[1]/div/div/div')
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", box,
                                   "b"
                                   "ackground-color: green;")
        ActionChains(self.driver).click_and_hold(point).move_by_offset(750, 300).perform()
        ActionChains(self.driver).click().perform()



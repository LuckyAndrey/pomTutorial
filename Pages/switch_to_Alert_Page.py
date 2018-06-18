import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Switch_to_Allert(object):

    def __init__(self, driver):
        self.driver = driver

    def curentPage_is(self):
        return  (self.driver.title, self.driver.current_url)

    def popUpWindow(self, variant):
        if variant == 'ok':
            print(self.driver.window_handles)
            alert = self.driver.switch_to.alert.accept()
        elif variant == 'ok_cancel':
            # self.driver.switch_to.alert
            alert = self.driver.switch_to.alert.dismiss()
            print(self.driver.window_handles)
            # alert.switch_to.alert.dismiss()
        elif variant == 'edit':
            pop = self.driver.switch_to.alert
            print(self.driver.window_handles)
            print(pop.text)
            pop.send_keys('TEst')
            time.sleep(2)
            pop.accept()
            print('Typed text:', self.driver.find_element_by_xpath('//*[@id="demo1"]').text)
            time.sleep(5)




    def choose_Alert_OK(self):
        s = self.driver.find_element_by_xpath(LocatorsAlert.alert_OK)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", s,
                               "color:green; background-color: tomato;")
        print(s)
        s.click()
        self.driver.find_element_by_xpath(LocatorsAlert.buttonOKTab).click()
        time.sleep(6)
        self.popUpWindow('ok')
        time.sleep(6)



    def choose_Alert_OK_Cancel(self):
        self.driver.find_element_by_xpath(LocatorsAlert.alert_OK_CANCEL).click()
        # Switch_to_Allert.commonButtonClick()
        self.driver.find_element_by_xpath(LocatorsAlert.commonButtonOK_Cancel).click()
        self.popUpWindow('ok_cancel')



    def Alert_TextBox(self):
        self.driver.find_element_by_xpath(LocatorsAlert.alert_TextBox).click()
        self.driver.find_element_by_xpath(LocatorsAlert.button_textbox).click()
        self.popUpWindow('edit')


class NewWindows(object):

    def __init__(self, driver):
        self.driver = driver

    def openNewTabWindow(self):
        self.driver.find_element_by_xpath(LocatorsAlert.topMenu).click()
        self.driver.find_element_by_xpath(LocatorsAlert.windowsMenu).click()
        self.driver.find_element_by_xpath(LocatorsAlert.openNewTabWindow).click()
        self.driver.find_element_by_xpath(LocatorsAlert.win_buttonClick).click()

    def openNewSeparateWindow(self):
        self.driver.find_element_by_xpath(LocatorsAlert.topMenu).click()
        self.driver.find_element_by_xpath(LocatorsAlert.windowsMenu).click()
        self.driver.find_element_by_xpath(LocatorsAlert.openNewSeparateWindow).click()
        self.driver.find_element_by_xpath(LocatorsAlert.btn_openNewSeparateWindow).click()

    def openSenarateMultyWindows(self):
        self.driver.find_element_by_xpath(LocatorsAlert.topMenu).click()
        self.driver.find_element_by_xpath(LocatorsAlert.windowsMenu).click()
        self.driver.find_element_by_xpath(LocatorsAlert.openSenarateMultyWindows).click()
        self.driver.find_element_by_xpath(LocatorsAlert.btn_openNewSeparateWindows).click()



class LocatorsAlert:
    url = 'http://demo.automationtesting.in/Alerts.html'
    alert_OK = '//*[@href="#OKTab"]'
    # alert_OK = '//a[@href="#OKTab"]'
    alert_OK_CANCEL = '//*[@href="#CancelTab"]'
    alert_TextBox = '//*[@href="#Textbox"]'
    buttonClick = '//*[@id="OKTab"]/button'
    buttonOKTab = '//*[@id="OKTab"]/button'
    commonButtonOK_Cancel = '//*[@id="CancelTab"]/button'
    button_textbox = '//*[@id="Textbox"]/button'


    # Windows ----------------------------------------------------------
    window_url = 'http://demo.automationtesting.in/Windows.html'
    topMenu = '//a[@href="SwitchTo.html"]'
    windowsMenu = '//a[@href="Windows.html"]'
    openNewTabWindow = '//a[@href="#Tabbed"]'
    btn_openNewSeparateWindow = '//*[@class="btn btn-primary"]'
    btn_openNewSeparateWindows = '//div[@id="Multiple"]/button[@class="btn btn-info"]'
    openNewSeparateWindow = '//a[@href="#Seperate"]'
    openSenarateMultyWindows = '//a[@href="#Multiple"]'
    win_buttonClick = '//a[@href="http://www.sakinalium.in"]'


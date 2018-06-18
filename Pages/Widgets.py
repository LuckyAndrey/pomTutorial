# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import time

class Accordion_Wigets(object):

    def __init__(self, driver):
        self.driver = driver

    def clickOnCollapsibleGroup1(self):
        self.driver.find_element_by_xpath(Locators.topMenu).click()
        self.driver.find_element_by_xpath(Locators.accordeon).click()
        self.driver.find_element_by_xpath(Locators.collaps1).click()
        return self.getText(Locators.collaps1_text)



    def getText(self, elem):
        print('Text '.center(90,'.'))
        txt = self.driver.find_element_by_xpath(elem).text
        print('Lenght of text = ',len(txt))
        print(txt)
        print('END '.center(90,'='))
        time.sleep(3)

    def clickOnCollapsibleGroup2(self):
        self.driver.find_element_by_xpath(Locators.topMenu).click()
        self.driver.find_element_by_xpath(Locators.accordeon).click()
        self.driver.find_element_by_xpath(Locators.collaps2).click()
        self.getText(Locators.collaps2_text)
        # self.driver.find_element_by_xpath(Locators.collaps2).click()

    def clickOnCollapsibleGroup3(self):
        self.driver.find_element_by_xpath(Locators.topMenu).click()
        self.driver.find_element_by_xpath(Locators.accordeon).click()
        self.driver.find_element_by_xpath(Locators.collaps3).click()
        self.getText(Locators.collaps3_text)
        # self.driver.find_element_by_xpath(Locators.collaps3).click()

    def clickOnCollapsibleGroup4(self):
        print(' 4')
        self.driver.find_element_by_xpath(Locators.topMenu).click()
        self.driver.find_element_by_xpath(Locators.accordeon).click()
        self.driver.find_element_by_xpath(Locators.collaps4).click()
        self.getText(Locators.collaps4_text)
        # self.driver.find_element_by_xpath(Locators.collaps4).click()




    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

class Windows(object):

    def __init__(self, driver):
        self.driver = driver

    def openNewTabWindow(self):
        self.driver.find_element_by_xpath(Locators.topMenu).click()
        self.driver.find_element_by_xpath(Locators.accordeon).click()
        self.driver.find_element_by_xpath(Locators.topMenu).click()

    def openNewSeparateWindow(self):
        self.driver.find_element_by_xpath(Locators.topMenu).click()
        self.driver.find_element_by_xpath(Locators.accordeon).click()
        self.driver.find_element_by_xpath(Locators.topMenu).click()

    def openSenarateMultyWindows(self):
        self.driver.find_element_by_xpath(Locators.topMenu).click()
        self.driver.find_element_by_xpath(Locators.accordeon).click()
        self.driver.find_element_by_xpath(Locators.topMenu).click()

class Locators:

    #  Accordion------------------------------------------------------

    url = 'http://demo.automationtesting.in/Accordion.html'
    topMenu = '//a[@href="Widgets.html"]'
    accordeon = '//a[@href="Accordion.html"]'

    collaps1 = '//div[@id="collapse1"]'
    collaps1_text = '//div[@id="collapse1"]/div'

    # collaps2 = '//*[@id="Functionality"]/div/div/div/div[2]/div[1]/h4/a/b'
    collaps2 = '//a[@href="#collapse2"]'
    collaps2_text = '//*[@id="collapse2"]/div'

    collaps3 = '//a[@href="#collapse3"]'
    collaps3_text = '//*[@id="collapse3"]/div'
    collaps4 = '//a[@href="#collapse4"]'
    collaps4_text = '//div[@id="collapse4"]/div'

    # Windows ----------------------------------------------------------

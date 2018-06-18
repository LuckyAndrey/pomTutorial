import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import requests




class RegisterPage(object):

    def __init__(self, driver):
        self.driver = driver

    def url(self):
        return "http://demo.automationtesting.in/Register.html"

    def type_user_name(self, firstName, lastName):
        self.elem = self.driver.find_element_by_xpath(Locators.fistName).click()
        self.driver.find_element_by_xpath("//input[@type='text']").clear()

        self.driver.find_element_by_xpath("//input[@type='text']").send_keys(firstName)

        self.driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        self.driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        self.driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys(lastName)


    def type_user_address_phone_email(self, address, phone, email):
        self.driver.find_element_by_xpath("//form[@id='basicBootstrapForm']/div[2]/div/textarea").click()
        self.driver.find_element_by_xpath("//form[@id='basicBootstrapForm']/div[2]/div/textarea").clear()
        self.driver.find_element_by_xpath("//form[@id='basicBootstrapForm']/div[2]/div/textarea").send_keys(address)

        self.driver.find_element_by_xpath("//input[@type='email']").click()
        self.driver.find_element_by_xpath("//input[@type='email']").clear()
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys(email)

        self.driver.find_element_by_xpath("//input[@type='tel']").clear()
        self.driver.find_element_by_xpath("//input[@type='tel']").send_keys(phone)

    def select_countries(self, countries):
        Select(self.driver.find_element_by_id("countries")).select_by_visible_text(countries)

    def select_country(self, country):
        Select(self.driver.find_element_by_id("country")).select_by_visible_text(country)

    def select_Male_radioButton(self):
        self.driver.find_element_by_xpath(Locators.maleRadiobutton).click()


    def select_Female_radioButton(self):
        self.driver.find_element_by_xpath(Locators.femaleRadiobutton).click()


    def click_checkboxes(self):
        self.driver.find_element_by_id("checkbox1").click()
        print(' Element is selected {}'.format(self.driver.find_element_by_id("checkbox1").is_selected()))

        self.driver.find_element_by_id("checkbox2").click()
        print(' Element is selected {}'.format(self.driver.find_element_by_id("checkbox2").is_selected()))
        self.driver.find_element_by_id("checkbox3").click()
        print(' Element is selected {}'.format(self.driver.find_element_by_id("checkbox3").is_selected()))

#-------------------------------------------------------------

    def skills(self): # get list of options
        skills = []
        skill = self.driver.find_elements_by_xpath('//*[@id="Skills"]/option')
        for i in skill:
            skills.append(i.get_attribute('value'))
        # s = skills.get_attribute('value')
        # print(skills)
        return skills


    def set_skills(self): # set value from list of options
        dataset = self.skills()
        # print(type(dataset))
        field = self.driver.find_element_by_id("Skills")
        for skill in dataset[1:]:
            self.driver.find_element_by_id("Skills").click()
            Select(self.driver.find_element_by_id("Skills")).select_by_visible_text(skill)
            self.driver.find_element_by_id("Skills").click()
            time.sleep(0.5)



    def set_languages(self):
        self.driver.find_element_by_id("msdd").click()
        self.driver.find_element_by_link_text("English").click()
        self.driver.find_element_by_link_text("German").click()
        self.driver.find_element_by_link_text("Urdu").click()

    def verify_now_many_languages_selected(self):
        return 'Chosen {} languages '.format(
            len(self.driver.find_elements_by_xpath(Locators.selected_languages)))


    def count_languages(self):  # return len of array
        return len(self.driver.find_elements_by_xpath(Locators.languages))


    def get_links(self, tag='a', attr='href'):
        hrefAttr = []
        links = self.driver.find_elements_by_tag_name(tag)
        for link in links:
            if link.get_property(attr) != None:
                hrefAttr.append(link.get_property(attr))
        return hrefAttr

    def checkLinks(self, hrefs):
        brokenLinks = []
        print("Total {} links".format(len(hrefs)))
        for link in hrefs:
            try:
                r = requests.get(link).status_code
                if (r != 200):
                    brokenLinks.append(('status ' + r, ' ---> ', link))
                    print(r, ' --->  ', link)
                else:
                    print("Link {} is valid".format(link))
            except:
                pass
        for i in brokenLinks:
            print(i)



class Locators:
    fistName = "//input[@type='text']"


    maleRadiobutton = '//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input'
    femaleRadiobutton = '//*[@id="basicBootstrapForm"]/div[5]/div/label[2]/input'
    languages = '//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li'
    selected_languages = '//*[@id="msdd"]/div'
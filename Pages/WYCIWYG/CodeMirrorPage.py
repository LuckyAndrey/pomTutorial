import time
from selenium.webdriver.common.action_chains import ActionChains

class CodeMirror(object):

    def __init__(self, driver):
        self.driver = driver


    def verifyTextFieldEmpty(self):
        if self.lineNumber() == 1:
            print('Empty text field')
            return True
        else:
            return False
        # return len(self.driver.find_elements_by_xpath(self.Locator.textField))

    def lineNumber(self):
        return self.driver.find_element_by_xpath(self.Locator.line_number)

    def enterLines(self, numsLines, text):
        xpath = self.Locator.line
        for i in range(1,numsLines+1):
            action = ActionChains(self.driver)
            line = self.driver.find_element_by_xpath(xpath + '[' + str(i) + ']')
            action.move_to_element(line)
            action.click()
            action.send_keys(text)

            # action.perform()
            if i < numsLines + 1:
                action.send_keys(u'\ue007')
                action.perform()
                time.sleep(1)
            else:
                break
            print('Sent text  ', text, ' Typed text ', self.driver.find_element_by_xpath(self.Locator.lineText).text)
            print('Lenght of text  ', len(self.driver.find_element_by_xpath(self.Locator.lineText).text))
            time.sleep(1)



    class Locator:

        url = 'http://demo.automationtesting.in/CodeMirror.html'
        textField = '//pre[@class=" CodeMirror-line "]'
        line =  '//div[@class="CodeMirror-code"]/div'
        lineText = '//div[@class="CodeMirror-code"]/div/pre/span'
        line_number = '//div[@class="CodeMirror-linenumber CodeMirror-gutter-elt"]'
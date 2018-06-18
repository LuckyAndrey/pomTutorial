import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(30)
url = 'http://demo.automationtesting.in/SummerNote.html'
# url = 'http://demo.automationtesting.in/CodeMirror.html'
driver.get(url)
#
# point = driver.find_element_by_xpath('//div[@class="CodeMirror-code"]/div/pre[@class=" CodeMirror-line "]/span')
# driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", point,

                               # "color:green; background-color: tomato;")
def ddd():
    kk= 6
    xp = '//div[@class="CodeMirror-code"]/div'
    text = "Hi"
    for i in range(1,kk):
        line = driver.find_element_by_xpath(xp+'['+str(i)+']')
        action = ActionChains(driver)
        action.move_to_element(line)
        action.click()
        time.sleep(1)
        action.send_keys(text)
        # action.perform()
        if i < kk+1:
            action.send_keys(u'\ue007')
            action.perform()
            time.sleep(1)
        else:
            break
# ddd()

def enterLines( numsLines, text):
    xpath = '//div[@class="note-editable panel-body"]/p'
    for i in range(1, numsLines):
        line = driver.find_element_by_xpath(xpath + '[' + str(i) + ']')
        action = ActionChains(driver)
        action.move_to_element(line)
        action.click()
        time.sleep(1)
        action.send_keys(text)
        action.send_keys(u'\ue007')
        action.perform()


# enterLines(20, 'hay')


def select_chars(ln, start, end):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    url = 'http://demo.automationtesting.in/SummerNote.html'
    driver.get(url)
    line = driver.find_element_by_xpath('//div[@class="note-editable panel-body"]/p'+'['+str(ln)+']').text
    lines = driver.find_element_by_xpath('//div[@class="note-editable panel-body"]/p[1]')
    print('line  ',len(line), line)
    char = line[start:end+1]
    firstchar = line[start]

    action = ActionChains(driver)
    action.move_to_element(lines).click().perform()
    action.click()
    # ac
    action.perform()

    action.send_keys(Keys.BACKSPACE*6)
    action.send_keys(Keys.CONTROL+'a')
    action.perform()
    print(driver.find_element_by_xpath('//div[@class="note-editable panel-body"]/p'+'['+str(ln)+']').text)
    print(len(driver.find_element_by_xpath('//div[@class="note-editable panel-body"]/p'+'['+str(ln)+']').text))

    print('char  ',len(char), char)

# select_chars(1,6,9)

def highlightElement(elem):
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", elem,
                          "color:red; background-color: white;")


def table(row = 3, column = 5):

    button = '//div[@class="note-btn-group btn-group note-table"]' \
             '//button[@class="note-btn btn btn-default btn-sm dropdown-toggle"] '
    btn = driver.find_element_by_xpath(button)
    highlightElement(btn)
    btn.click()
    e = driver.find_element_by_xpath('//div[@class="note-dimension-picker"]'
                                 '/div[@class="note-dimension-picker-highlighted"]')
    highlightElement(e)
    act = ActionChains(driver)
    act.move_to_element(e)
    # time.sleep(5)
    act.move_by_offset(160,160)
    act.click()
    act.perform()


def showElement(elem):
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", elem,
                              "color:green; background-color: green;")

def select_All():
    element = ''
    keys = ''
    element = driver.find_element_by_xpath('//div[@class="note-editable panel-body"]/p')
    txt = element.text
    highlightElement(element)
    action = ActionChains(driver)
    action.move_to_element(element).click().perform()
    action.send_keys(Keys.CONTROL + '\u0061')
    action.send_keys(Keys.DELETE)
    action.perform()
    # for i in range(len(txt)):
    #     pass
        # time.sleep(3)
        # action.click().perform()

select_All()
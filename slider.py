import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import pointer_actions

driver = webdriver.Chrome()
driver.get('https://jqueryui.com/slider/')
driver.switch_to.frame(0)
slider = driver.find_element_by_xpath('//*[@id="slider"]/span')
act = ActionChains(driver)
act.drag_and_drop_by_offset(slider, 0 ,0).perform()
# time.sleep(5)


prop = int(driver.execute_script('return document.getElementsByClassName("ui-slider-handle ui-corner-all ui-state-default")[0].style.left;').split('%')[0])
print('start ', prop)

while int(driver.execute_script('return document.getElementsByClassName'
                             '("ui-slider-handle ui-corner-all ui-state-default")'
                                '[0].style.left;').split('%')[0]) != 100 :
    propleft = slider.value_of_css_property('left')
    prop = int(driver.execute_script('return document.getElementsByClassName'
                              '("ui-slider-handle ui-corner-all ui-state-default")'
                              '[0].style.left;').split('%')[0])
    act.drag_and_drop_by_offset(slider, 50 ,0).perform()
    print('now ', prop, '%', 'pixels ', propleft)
time.sleep(5)

prop = int(driver.execute_script('return document.getElementsByClassName'
                                 '("ui-slider-handle ui-corner-all ui-state-default")[0].style.left;').split('%')[0])
propleft = slider.value_of_css_property('left')
print('end ', prop, 'pixels ', propleft)


driver.close()
driver.quit()
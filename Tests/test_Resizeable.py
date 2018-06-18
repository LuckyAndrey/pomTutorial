from selenium import webdriver
from Pages.Interactions.resizeable import Resize

class ResizeBox():
    driver = webdriver.Chrome()
    driver.get('http://demo.automationtesting.in/Resizable.html')
    page = Resize(driver)
    page.increase_size()



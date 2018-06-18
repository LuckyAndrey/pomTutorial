import time
import unittest

from selenium import webdriver

from Pages.switch_to_Alert_Page import NewWindows
from Pages.switch_to_Alert_Page import Switch_to_Allert, LocatorsAlert


class test_Switch_to_Alert(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):

        cls.driver.close()
        cls.driver.quit()

    # def test_rightPage(self):
    #     pass

    def test_AlertOK(self):
        driver = self.driver
        driver.get(LocatorsAlert.url)
        alertOK = Switch_to_Allert(driver)
        self.assertEqual(alertOK.curentPage_is(), ('Alerts', LocatorsAlert.url))
        alertOK.choose_Alert_OK()
        time.sleep(5)
        # driver.switch_to.alert.send_keys()

    def test_Alert_OK_Cancel(self):
        driver = self.driver
        driver.get(LocatorsAlert.url)

        alertOkCancel = Switch_to_Allert(driver)
        alertOkCancel.choose_Alert_OK_Cancel()
        time.sleep(5)

    def test_alerttext(self):
        driver = self.driver
        driver.get(LocatorsAlert.url)

        alertText = Switch_to_Allert(driver)
        alertText.Alert_TextBox()
        time.sleep(5)


    def test_TabWindow(self):
        driver = self.driver
        driver.get(LocatorsAlert.window_url)

        win = NewWindows(driver)
        win.openNewTabWindow()
        w = driver.window_handles
        w = driver.switch_to_window(w[1])
        print('window ',(w), '  current_url  ',driver.current_url)
        time.sleep(5)

    def test_OneSeparateWindow(self):
        driver = self.driver
        driver.get(LocatorsAlert.window_url)

        win = NewWindows(driver)
        win.openNewSeparateWindow()
        time.sleep(5)
        w = driver.window_handles
        w = driver.switch_to_window(w[1])
        print('window ',(w), '  current_url  ',driver.current_url)
        # print(w)
        self.assertEqual(driver.current_url, 'http://www.sakinalium.in/')

    def test_multySeparatedWwindow(self):
        driver = self.driver
        driver.get(LocatorsAlert.url)

        win = NewWindows(driver)
        win.openSenarateMultyWindows()
        w = driver.window_handles
        print(" windows opened  ", len(w))
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
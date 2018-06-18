

class Page(object):

    def __init__(self, driver):
        self.driver = driver

    def corretPage(self):
        return (self.driver.title, self.driver.current_url)
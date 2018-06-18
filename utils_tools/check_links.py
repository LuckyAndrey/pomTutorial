import requests
from    selenium import webdriver



class BrokenLink(object):

    def __init__(self, driver):
        self.driver = driver


    def broken_links(self):
        hrefs = []
        links = self.driver.find_elements_by_tag_name('a')
        print("Found {} links".format(len(links)))
        # print(links)

        for i in links:
            if i.get_property('href') != None:
                hrefs.append(i.get_property('href'))
        # print(hrefs)
        for i in hrefs:
            print('endswith  ',str(i).endswith('htlm'), '  ',i)
            if str(i).endswith('htlm') == True:
                continue
            else:
                print('False ',i)
                continue
        for link in sorted(hrefs):

            r = requests.get(link)
            # print(type(r.status_code))
            if r.status_code >= 200 and r.status_code <= 308:
                continue
            else:
                print('Response {}'.format(r),'  Broken link ', link)































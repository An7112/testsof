from selenium.webdriver.common.keys import Keys

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def enter_search_text(self,searchtext):
        return self.driver.find_element_by_name("search_query").send_keys(searchtext)
    def press_return_key_search_field(self):
        return self.driver.find_element_by_name('search_query').send_keys(Keys.ENTER)
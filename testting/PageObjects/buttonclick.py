
button_xpath ="/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer"
class Button:

    def __init__(self, driver):
        self.driver = driver

    def test_button_text1(self):
        return self.driver.find_element_by_link_text("Explore").click()
    def test_button_text2(self):
        return self.driver.find_element_by_link_text("Shorts").click()
    def test_button_text3(self):
        return self.driver.find_element_by_link_text("Subscriptions").click()
    def test_button_text4(self):
        return self.driver.find_element_by_link_text("Library").click()
    def test_button_text5(self):
        return self.driver.find_element_by_link_text("History").click()
    def test_button_text6(self):
        return self.driver.find_element_by_xpath(button_xpath).click()

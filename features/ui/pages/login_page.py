from features.ui.all_imports import *
from features.ui.pages.base_page import BasePage

class Login(BasePage):

    # LOCATORS
    username_box = "//input[@id='username']"
    password_box = "//input[@id='password']"
    login_button =  "//i[@class='fa fa-2x fa-sign-in']"

    # ACTIONS ON THE PAGE
    def enter_username(self, uname):
        self.enter_text_by_xpath(self.username_box, uname)

    def enter_password(self, phrase):
        self.enter_text_by_xpath(self.password_box, phrase)

    def click_login(self):
        self.click_element_by_xpath(self.login_button)

    @property
    def get_title(self):
        return self.driver.title

class PopUpWindow(BasePage):

    openwindow_button = "//button[@id='openwindow']"
    search_box = "//input[@id='search-courses']"


    def click_openwindow(self):
        self.click_element_by_xpath(self.openwindow_button)

    def search_text(self, text):
        element = self.driver.find_element_by_xpath(self.search_box)
        element.clear()
        element.send_keys(text)
        element.submit()

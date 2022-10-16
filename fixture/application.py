from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper
from fixture.contact import ContactHelper
from fixture.navigation import NavigationHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        self.wd.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.navigation = NavigationHelper(self)

    def destroy(self):
        self.wd.quit()


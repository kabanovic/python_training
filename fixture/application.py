from selenium import webdriver
from fixture.session import Session
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.webdriver.common.by import By

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(10)
        self.session = Session(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if wd.current_url.endswith("/index.php"):
            return
        wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()
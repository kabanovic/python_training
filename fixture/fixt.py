from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.sess import Sess
from fixture.contact import ContactHelper
class Applicat:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.sess = Sess(self)
        self.contact = ContactHelper(self)

    def home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def destr(self):
        self.wd.quit()
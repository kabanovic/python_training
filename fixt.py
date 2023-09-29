from selenium import webdriver
from selenium.webdriver.common.by import By

class Applicat:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_home_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def add_contact(self, contact):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(contact.telephone)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_home_page()

    def login(self, username, password):
        wd = self.wd
        self.home_page()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def destr(self):
        self.wd.quit()
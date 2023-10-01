from selenium.webdriver.common.by import By

class ContactHelper:

    def __init__(self, appl):
        self.appl = appl

    def return_home_page(self):
        wd = self.appl.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def add(self, contact):
        wd = self.appl.wd
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
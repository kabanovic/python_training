from selenium.webdriver.common.by import By

class ContactHelper:

    def __init__(self, app):
        self.app = app



    def return_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def add(self, contact):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.contact(contact)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_home_page()


    def delete_first_cont(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()


    def edit_first_cont(self, contact):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        self.contact(contact)
        wd.find_element(By.NAME, "update").click()
        self.return_home_page()

    def contact(self, contact):
        wd = self.app.wd
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
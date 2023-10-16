from selenium.webdriver.common.by import By
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def add(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.fill_contact_form(contact)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_home_page()

    def delete_first_cont(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def edit_first_cont(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        wd.find_element(By.NAME, "update").click()
        self.return_home_page()

    #def contact(self, contact):
     #   wd = self.app.wd
     #   wd.find_element(By.NAME, "firstname").click()
     #   wd.find_element(By.NAME, "firstname").clear()
     #   wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
     #   wd.find_element(By.NAME, "middlename").clear()
     #   wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
     #   wd.find_element(By.NAME, "lastname").clear()
     #   wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
     #   wd.find_element(By.NAME, "mobile").click()
     #   wd.find_element(By.NAME, "mobile").clear()
     #   wd.find_element(By.NAME, "mobile").send_keys(contact.telephone)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_field("firstname", contact.firstname)
        self.change_contact_field("middlename", contact.middlename)
        self.change_contact_field("lastname", contact.lastname)
        self.change_contact_field("mobile", contact.telephone)

    def change_contact_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def count_cont(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements(By.XPATH, "//img[@alt='Edit']"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contacts = []
        for element in wd.find_elements(By.NAME, "entry"):
            # text = element.text
            cells = element.find_elements(By.TAG_NAME, "td")
            id = cells[0].find_element(By.NAME, "selected[]").get_attribute("value")
            firstname = cells[2].text
            lastname = cells[1].text
            contacts.append(Contact(firsname=firstname, lastname=lastname, id=id))
        return contacts
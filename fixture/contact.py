from selenium.webdriver.common.by import By
from model.contact import Contact
import re


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
        self.cont_cache = None

    def delete_first_cont(self):
        self.delete_some_cont(0)

    def delete_some_cont(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements(By.NAME, "selected[]")[index].click()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.cont_cache = None

    def delete_some_cont_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.cont_cache = None

    def add_some_cont_to_group(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()
        wd.find_element(By.XPATH, "//input[@value='Add to']").click()
        self.cont_cache = None

    def select_group_for_del_cont(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME, "group").click()
        wd.find_element(By.XPATH, f"//option[@value={index}]").click()

    def del_some_cont_from_group(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()
        wd.find_element(By.NAME, "remove").click()
        wd.find_element(By.XPATH, "//i/a").click()
        #wd.find_element(By.LINK_TEXT, f'a[href="/?group={id}"]').click()
        self.cont_cache = None

    def edit_first_cont(self, contact):
        self.edit_some_cont(0)

    def edit_some_cont(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()
        self.fill_contact_form(contact)
        wd.find_element(By.NAME, "update").click()
        self.return_home_page()
        self.cont_cache = None

    def edit_some_cont_by_id(self, id, contact):
        wd = self.app.wd
        self.app.open_home_page()
        #wd.find_element(By.CSS_SELECTOR, f"a[href='edit.php?id={id}']").click()
        wd.find_element(By.CSS_SELECTOR, "a[href='edit.php?id=%s']" % id).click()
        self.fill_contact_form(contact)
        wd.find_element(By.NAME, "update").click()
        self.return_home_page()
        self.cont_cache = None

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
        #self.change_contact_field("home", contact.homephone)
        #self.change_contact_field("mobile", contact.telephone)

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

    cont_cache = None

    def get_contact_list(self):
        if self.cont_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.cont_cache = []
            for element in wd.find_elements(By.NAME, "entry"):
                cells = element.find_elements(By.TAG_NAME, "td")
                id = cells[0].find_element(By.NAME, "selected[]").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                all_phones = cells[5].text
                adress = cells[3].text
                all_mails = cells[4].text
                self.cont_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, adress=adress,
                                               all_phones_from_home_page=all_phones, all_mails=all_mails))
        return list(self.cont_cache)

    def open_contact_to_edit(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()

    def open_contact_view(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        adress = wd.find_element(By.NAME, "address").get_attribute("value")
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        homephone = wd.find_element(By.NAME, "home").get_attribute("value")
        workphone = wd.find_element(By.NAME, "work").get_attribute("value")
        mobilephone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        secondaryphone = wd.find_element(By.NAME, "phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, adress=adress, homephone=homephone,
                       workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone,
                       email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view(index)
        text = wd.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)
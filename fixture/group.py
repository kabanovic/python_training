from selenium.webdriver.common.by import By

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups()
        # create new group
        wd.find_element(By.NAME, "new").click()
        # fill form
        self.fill_group_form(group)
        # submit group
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field("group_name", group.name)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)


    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def edit_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups()
        # choose group
        self.select_first_group()
        wd.find_element(By.NAME, "edit").click()
        # fill form
        self.fill_group_form(new_group_data)
        # update group
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups()
        self.select_first_group()
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups()

    def open_groups(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()


    def count(self):
        wd = self.app.wd
        self.open_groups()
        return len(wd.find_elements(By.NAME, "selected[]"))

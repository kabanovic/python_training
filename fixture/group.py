from selenium.webdriver.common.by import By
from model.group import Group
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
        self.group_cache = None

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
        self.edit_some_group(0)

    def edit_some_group(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups()
        # choose group
        self.select_some_group(index)
        wd.find_element(By.NAME, "edit").click()
        # fill form
        self.fill_group_form(new_group_data)
        # update group
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]").click()

    def select_some_group(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def delete_first_group(self):
        self.delete_some_group(0)

    def delete_some_group(self, index):
        wd = self.app.wd
        self.open_groups()
        self.select_some_group(index)
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups()
        self.group_cache = None

    def open_groups(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new")) > 0:
            return
        wd.find_element(By.LINK_TEXT, "groups").click()

    def count_group(self):
        wd = self.app.wd
        self.open_groups()
        return len(wd.find_elements(By.NAME, "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups()
            self.group_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
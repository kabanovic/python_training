from selenium.webdriver.common.by import By

class Sess:

    def __init__(self, appl):
        self.appl = appl

    def login(self, username, password):
        wd = self.appl.wd
        self.appl.home_page()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def logout(self):
        wd = self.appl.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()
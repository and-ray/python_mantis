from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element("name", "username").click()
        wd.find_element("name","username").clear()
        wd.find_element("name","username").send_keys(username)
        wd.find_element("name","password").clear()
        wd.find_element("name","password").send_keys(password)
        wd.find_element(By.XPATH,"//input[@value='Login']").click()

    def is_logged_in_as(self, username):
        return self.get_logged_user() ==username


    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR,"td.login-info-left span").text

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT,'Logout')) > 0

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT,'Logout').click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

from pom.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from pom.login_page import LoginPage

class MainPage(BaseDriver):

    def go_to_login_page(self):
        self.driver.find_element(By.LINK_TEXT,'登录').click()
        return LoginPage()
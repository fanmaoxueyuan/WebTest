import os
from selenium import webdriver
from selenium.webdriver.common.by import By

from pom.base_driver import BaseDriver


class LoginPage(BaseDriver):
    _username = (By.ID,'name')
    _password = (By.ID,'pass')


    def login_with_username(self,username,passwd):
        self.driver.find_element(*LoginPage._username).send_keys(username)
        self.driver.find_element(By.ID,'pass').send_keys(passwd)
        self.driver.find_element(By.CSS_SELECTOR,'[value="登录"]').click()


if __name__ == '__main__':
    from pom.main_page import MainPage
    mp = MainPage()
    lp = mp.go_to_login_page()
    lp.login_with_username('zhangsan','123456')
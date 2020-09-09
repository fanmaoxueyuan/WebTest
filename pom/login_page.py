import os
from selenium import webdriver
from selenium.webdriver.common.by import By

from pom.base_driver import BaseDriver
from pom.resetpasswd_page import ResetPasswdPage


class LoginPage(BaseDriver):
    _username = (By.ID,'name')
    _password = (By.ID,'pass')


    def login_with_username(self,username,passwd):
        self.driver.find_element(*LoginPage._username).send_keys(username)
        self.driver.find_element(*LoginPage._password).send_keys(passwd)
        self.driver.find_element(By.CSS_SELECTOR,'[value="登录"]').click()


    def go_reset_passwd_page(self):
        self.driver.find_element(By.LINK_TEXT,'忘记密码了?').click()
        return ResetPasswdPage()

if __name__ == '__main__':
    from pom.main_page import MainPage
    mp = MainPage()
    lp = mp.go_to_login_page()
    lp.login_with_username('zhangsan','123456')
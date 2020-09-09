from selenium.webdriver.common.by import By

from pom.base_driver import BaseDriver


class ResetPasswdPage(BaseDriver):

    def reset_passwd(self,email):
        self.driver.find_element(By.ID,'email').send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR,'[value="提交"]').click()
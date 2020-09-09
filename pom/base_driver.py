import os
from  selenium import  webdriver


class BaseDriver:
    driver = None
    def __init__(self):
        if not BaseDriver.driver:
            driverpath = os.path.join(os.path.dirname(__file__), '../drivers/chromedriver.exe')
            self.driver = webdriver.Chrome(executable_path=driverpath)
            BaseDriver.driver = self.driver
            self.driver.maximize_window()
            self.driver.get('http://49.233.108.117:3000/')

        self.driver = BaseDriver.driver

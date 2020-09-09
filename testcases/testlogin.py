import unittest
from pom.main_page import MainPage

# 继承TestCase
class TestLoginCase(unittest.TestCase):

    def test_login_failed(self):
        mp = MainPage()
        lp = mp.go_to_login_page()
        lp.login_with_username('zhangsan','123456')
        # 对登录结果进行验证
        fail_text = lp.login_fail_text()
        assert fail_text == "用户名或密码错误"



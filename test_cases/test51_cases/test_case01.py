import unittest
from time import sleep

from ddt import ddt, data, unpack
from selenium import webdriver

from po.test51_po.home_page import HomePage
from po.test51_po.login_page import LoginPage


@ddt
class TestCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:

        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        # cls.hp = HomePage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        # sleep(3)
        cls.driver.quit()

    # def test_jump(self):
    #     self.hp.jump_login()
    #     self.assertTrue(True)

    @data(['知鱼', 'cxy123!@#'])
    @unpack
    def test_01_login(self, user, pwd):
        result = self.lp.login(user, pwd)
        self.assertTrue(result)

    # def test_02_task(self):
    #     result = self.hp.jump_to_task()
    #     self.assertTrue(result)
    #
    # def test_03_logout(self):
    #     result = self.hp.logout()
    #     self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

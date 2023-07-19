from selenium import webdriver

from base.base_page import BasePage
from po.test51_po.home_page_element import HomePageElement


class LoginPage(BasePage,HomePageElement):
    # url拼接的话，方便后面更改服务器
    url = 'http://bbs.51testing.com/member.php?mod=logging&action=login'
    # 封装成元组或字典都行
    username = ('name', 'username1')
    password = ('name', 'password')
    button=('name','loginsubmit')

    def login(self, _username, _password):
        self._open(self.url)
        self._input(self.username, txt=_username)
        self._input(self.password, txt=_password)
        self._click(self.button)
        self._sleep()
        return self._find_by_explicit_wait(self.exit_)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.login('知鱼', 'cxy123!@#')

from base.base_page import BasePage


# Cxy123!@#

class LoginPage(BasePage):
    url = 'https://accounts.qingflow.com/acc/passport/login'
    login_by_pwd_btn = ('xpath', '//div/a[text()=" 账号密码登录 "]')
    phonenum_box=('xpath','//input[contains(@placeholder,"手机号")]')
    # phonenum_box = ('xpath', '//input[contains(@placeholder,"密码")]/preceding-sibiling::input')

    pwd_box = ('xpath', '//input[contains(@placeholder,"密码")]')
    login_btn = ('xpath', '//span[text()=" 登录 "]')

    def login(self, info):
        self._open(self.url)
        self._click(self.login_by_pwd_btn)
        self._input(self.phonenum_box, txt=info['phonenum'])
        self._input(self.pwd_box, txt=info['password'])
        self._click(self.login_btn)
        self._save_img('login.png')

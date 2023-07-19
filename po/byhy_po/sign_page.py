from base.base_page import BasePage


class SignPage(BasePage):
    url = BasePage.url + 'mgr/sign.html'
    username_box = ('id', 'username')
    password_box = ('id', 'password')
    submit_btn = ('xpath', '//button[text()="登录"]')
    forgot_btn = ('xpath', '//*[contains(text(),"忘记密码")]')
    new_account_btn = ('xpath', '//*[contains(text(),"新账号")]')
    sign_flag = ('id', 'root')

    def log_in(self, userinfo):
        self._open(SignPage.url)
        self._input(SignPage.username_box, txt=userinfo['username'])
        self._input(SignPage.password_box, txt=userinfo['password'])
        self._click(SignPage.submit_btn)
        return self._find(SignPage.sign_flag)

    def new_account(self):
        pass

    def forgot_password(self):
        pass

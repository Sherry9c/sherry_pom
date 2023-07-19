from time import sleep

from selenium import webdriver

from base.base_page import BasePage
from po.bili_po.home_page_element import HomePageElement
from common.ChromeOptions import options


# 英文bilibili

class HomePage(BasePage, HomePageElement):
    url='https://www.bilibili.tv/en'

    # 跳转登录
    def login_by_email(self,email,pwd):
        checkbox = ('xpath', '//label[@class="bstar-checkbox"]')
        account=('xpath','//div[@class="login-tabs"]//button[text()="Account"]')
        input_email=('xpath','//input[@placeholder="Email"]')
        input_password=('xpath','//input[@placeholder="Enter Password"]')
        login_button=('xpath','//div[@class="login-account"]/button[text()="Log in"]')


        self._open(self.url)
        self._click(*self.jump_to_login_bt)
        self._click(*checkbox)
        # 登录方式选择，用contains定位不到
        self._click(*self.login_by_phone_email)
        self._click(*account)
        self._input(*input_email,txt=email)
        self._input(*input_password,txt=pwd)
        self._click(*login_button)

        return self._find_by_explicit_wait(*self.user_img)


    # 登出
    def logout(self):
        pass

    def jump_to_profile(self):
        self._open(self.url)
        self._move_and_click(self.user_img, self.profile_bt)

    #勾选协议
    def check_policy(self):
        pass



if __name__ == '__main__':
    op = options()
    driver = webdriver.Chrome(options=op)
    driver.implicitly_wait(5)
    hp = HomePage(driver)
    hp.jump_to_profile()
    sleep(3)
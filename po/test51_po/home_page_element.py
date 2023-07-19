from selenium import webdriver

from base.base_page import BasePage

class HomePageElement:

    jump_login = ('xpath', '//button/em[text()="登录"]')
    exit_ = ('xpath', '//p/a[text()="退出"]')
    download=('id','mn_N7b8e')
    # task=('xpath','//li/a[text()="积点任务"]')
    task = ('id', 'mn_Ne35a')
    search = ('id', 'scbar_txt')

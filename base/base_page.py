# 常用操作行为
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from common.file_handler import path_create, filename_duplicates
from common.logger import Logger
from common.ChromeOptions import options


# 可以将基类下面的函数定义为私有函数，更规范（函数名前加两个下划线）
class BasePage:
    url = 'http://127.0.0.1:82/'
    err_img_dir = '../logs/img/'
    test_img_dir = 'E:/result/img/'

    def __init__(self, driver):
        # self.driver = open_browser(type_)
        self.driver = driver
        self.log = Logger()
        self.driver.implicitly_wait(5)

    # def __init__(self, opt=True):
    #     # self.driver = open_browser(type_)
    #     if opt:
    #         self.driver = webdriver.Chrome(options=options())
    #     else:
    #         self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(5)
    #     self.log = Logger()

    def _open(self, url):
        self.log.info(f'正在打开url: {url}')
        self.driver.get(url)
        self.log.info('url已跳转')

    def _current_url(self):
        return self.driver.current_url

    def _find(self, el, t=3, ts=0.5):
        try:
            return WebDriverWait(self.driver, t, ts).until(lambda e: self.driver.find_element(*el),
                                                           message='元素获取失败')
        except Exception as e:
            img_name = '{0:.20s}.png'.format(e.msg.split(":")[0])
            self._save_img(img_name, type='err')
            self.log.info(f'{el}元素查找失败，已截图')
            return None

    def _find_all(self, el, t=3, ts=0.5):
        elements = WebDriverWait(self.driver, t, ts).until(lambda e: self.driver.find_elements(*el),
                                                           message='元素获取失败')
        return elements

    def _click(self, el):
        self.log.info(f'点击元素{el}')
        self._find(el).click()

    def _input(self, el, txt):
        self.log.info(f'正在向{el}中输入"{txt}"')
        element = self._find(el)
        element.clear()
        element.send_keys(txt)

    def _get_text(self, el):
        return self._find(el).text

    # 显示等待
    # def _wait_element(self, el, time, ts):
    #     return WebDriverWait(self.driver, time, ts).until(lambda e: self.driver.find_element(*el),
    #                                                       message='元素获取失败')

    def _save_img(self, filename, type=None):
        if type:
            file = f'{path_create(BasePage.err_img_dir)}{time.strftime("%m%d%H%M%S")}_{filename}'
        else:
            file = f'{path_create(BasePage.test_img_dir)}{time.strftime("%m%d%H%M%S")}_{filename}'
        file = filename_duplicates(file)
        self.log.info(f'截图生成:{file}')
        return self.driver.save_screenshot(file)

    # 显示等待的方式判断元素
    # def _find_by_explicit_wait(self, el, time=5, ts=0.5):
    #     try:
    #         self._wait_element(el, time, ts)
    #         return True
    #     except:
    #         return False

    # 强制等待
    def _sleep(self, t=3):
        self.log.info(f'sleep {t} s')
        time.sleep(t)

    def _quit(self):
        self.log.info('退出浏览器')
        self.driver.quit()

    def _assert_text(self, el, expected):
        try:
            reality = self._find(el).text
            assert expected == reality, f'{expected}与{reality}不等'
            return True
        except:
            return False

    # 切换句柄、iframe...
    def _switch_to_window(self, i):
        try:
            self.log.info(f'切换到第{i}个窗口')
            self.driver.switch_to.window(self.driver.window_handles[i])
            return True
        except Exception as e:
            self.log.error(f'切换窗口失败。错误信息:{e}')
            return False

    def _switch_to_iframe(self):
        pass

    def _switch_to_alert(self):
        try:
            self.log.info('切换到alert弹窗')
            return self.driver.switch_to.alert
        except Exception as e:
            self.log.error(f'弹窗切换失败：{e}')

    def _alert_accept(self, alert=None):
        if not alert:
            alert = self._switch_to_alert()
        self.log.info('alert弹窗点击确定')
        alert.accept()

    def _alert_dismiss(self, alert=None):
        if not alert:
            alert = self._switch_to_alert()
        self.log.info('alert弹窗点击取消')
        alert.dismiss()

    def _alert_input(self, txt, alert=None):
        if not alert:
            alert = self._switch_to_alert()
        self.log.info(f'alert弹窗中输入{txt}')
        alert.send_keys(txt)

    def _alert_txt(self, alert=None):
        if not alert:
            alert = self.driver.switch_to.alert
        txt = alert.text
        self.log.info(f'获取alert弹窗内容为：{txt}')
        return txt

    # 下拉框操作
    def _select_option_by_text(self, select, txt):
        select_box = self._find(select)
        try:
            Select(select_box).select_by_visible_text(txt)
            self.log.info(f'选择内容为"{txt}"的选项')
            return True
        except Exception as e:
            self.log.error(f'下拉框的{txt}选项选择失败')
            return False

    def _select_option_by_index(self, select, index):
        select_box = self._find(select)
        try:
            Select(select_box).select_by_index(index)
            self.log.info(f'选择下拉框的第{index}个选项')
            return True
        except Exception as e:
            self.log.error(f'下拉框的第{index}个选项选择失败')
            return False

    def _select_option_by_value(self, select, value):
        select_box = self._find(select)
        try:
            Select(select_box).select_by_index(value)
            self.log.info(f'选择下拉框中value为{value}的选项')
            return True
        except Exception as e:
            self.log.error(f'选择下拉框中value为{value}的选项失败')
            return False

    # 鼠标操作
    def _move_to_element(self, el):
        ActionChains(self.driver).move_to_element(self._find(el)).perform()

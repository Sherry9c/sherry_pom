from time import sleep

from base.base_page import BasePage


class IndexPage(BasePage):
    url = 'https://qingflow.com/index/2576352/dashboard/01c2c8fd'
    task_refresh_btn = ('xpath', '//div[@id="-6"]/div/i[1]')
    task_expand_btn = ('xpath', '//div[@id="-6"]/div/i[2]')

    mytask_share_btn = ('xpath', '//header/ul/li[1]')
    mytask_refresh_btn = ('xpath', '//header/ul/li[2]')
    mytask_edit_btn = ('xpath', '//header/ul/li[3]')
    mytask_exit_full_screen_btn = ('xpath', '//header/ul/li[4]')

    def task_expand_and_exit_full_screen(self):
        self._open(self.url)
        sleep(5)
        self._click(self.task_refresh_btn)
        self._click(self.task_expand_btn)
        self._click(self.mytask_refresh_btn)

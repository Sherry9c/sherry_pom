from base.base_page import BasePage
from po.test51_po.home_page_element import HomePageElement


class HomePage(BasePage, HomePageElement):

    url='http://bbs.51testing.com/forum.php'

    search_result = ('xpath', '//div[@class="sttl mbn"]/h2/em/span')

    def search(self, txt):
        self._open(self.url)
        self._click(*self.search, txt=txt)
        self._switch_to_window(-1)
        return txt == self._get_text(*self.search_result)

    def jump_to_login(self):
        self._open(self.url)
        self._click(*self.jump_login)
        # return self._find_by_explicit_wait(*self.exit_)
        # return LoginPage()

    def logout(self):
        self._open(self.url)
        self._click(*self.exit_)
        return self._find_by_explicit_wait(*self.jump_login)

    def jump_to_task(self):
        self._open(self.url)
        self._click(*self.task)
        return self.driver.current_url == BasePage.url + 'home.php?mod=task'

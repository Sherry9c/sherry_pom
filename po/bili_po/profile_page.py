from base.base_page import BasePage


class ProfilePage(BasePage):
    url = BasePage.url + 'account/setting'

    nickname = ('xpath', '//input[@placeholder="Please enter your nickname."]')
    date = ('xpath', '//input[@placeholder="Select date"]')
    bio = ('xpath', '//textarea[contains(@placeholder,"introduce")]')
    update_bt = ('xpath', '//button[text()="Update"]')

    def __init__(self):
        self._open(self.url)

    def _input_name(self, userinfo):
        self._input(*self.nickname, userinfo[0])
        self._input(*self.date, userinfo[1])
        self._input_name(*self.bio, userinfo[2])
        self._click(*self.update_bt)

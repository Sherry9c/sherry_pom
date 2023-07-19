import pytest
from selenium import webdriver

from common.file_handler import read_yaml
from po.byhy_po.sign_page import SignPage

data = read_yaml('../data/byhy/customer.yaml')


class TestSign:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.page = SignPage(self.driver)

    def teardown(self):
        self.page._quit()

    @pytest.mark.parametrize('userinfo', data['userinfo'])
    def test_sign(self, userinfo):
        result = self.page.log_in(userinfo)
        assert result

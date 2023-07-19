import pytest
from selenium import webdriver

from common.file_handler import read_yaml
from po.byhy_po.customer_page import CustomerPage
from po.byhy_po.sign_page import SignPage

datas = read_yaml('../data/byhy/customer.yaml')


class TestCustomer:
    # @pytest.fixture()
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.page = CustomerPage(self.driver)
        self.login = SignPage(self.driver).log_in(datas['userinfo'][0])

    def teardown_class(self):
        self.page._quit()

    # @pytest.fixture(autouse=True, scope='module')
    # @pytest.mark.usefixtures('setup_class')
    # # @pytest.mark.parametrize('userinfo', data['userinfo'])
    # def login(self):
    #     return self.login_page.log_in(data['userinfo'])

    # @pytest.mark.usefixtures('login')
    @pytest.mark.parametrize('content', datas['search'])
    # @pytest.mark.parametrize('content', ['深圳','武汉'])
    def test_search(self, content):
        t = self.page.search(content)
        assert t

    @pytest.mark.parametrize('data', datas['add'])
    def test_add_customer(self, data):
        result = self.page.add_customer(data['customer_info'])
        expected = data['expected']
        assert result['flag'] == expected['flag']
        assert expected['pop-up'] == result['pop-up']

    @pytest.mark.parametrize('data', datas['add-illegal'])
    def test_add_customer_illegal(self, data):
        result = self.page.add_customer(data['customer_info'])
        expected = data['expected']
        assert result['flag'] == expected['flag']
        assert expected['pop-up'] in result['pop-up']

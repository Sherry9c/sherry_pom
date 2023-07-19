import pytest
from selenium import webdriver
from common.ChromeOptions import options
from po.qingflow.index_page import IndexPage
from po.qingflow.login_page import LoginPage
from common.file_handler import read_yaml

data = read_yaml('../data/qingflow/index.yaml')


class TestIndex:
    # @pytest.fixture(scope='class')
    # def driver_(self):
    #     self.driver = webdriver.Chrome(options=options())
    #     return self.driver

    # @pytest.fixture(autouse=True, scope='class')
    # def login(self, TestIndex.driver):
    #     self.lp = LoginPage(TestIndex.driver)
    #     self.lp.login(data['userinfo'])

    # ip = IndexPage(TestIndex.driver)

    def setup_class(self):
        self.driver = webdriver.Chrome(options=options())

        self.ip = IndexPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.lp.login(data['userinfo'])


    def test_task_expand_and_exit_full_screen(self):
        self.ip.task_expand_and_exit_full_screen()

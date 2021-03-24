import pytest

import page
from base.driver import Driver
from base.getdata import get_data
from base.logger import Logger
from page.pagein import PageIn
from parameterized import parameterized

class TestBackLogin:
    def setup(self):
        self.driver=Driver().get_driver(page.url_back)
        self.pagein=PageIn(self.driver)
        self.PageBackLogin=self.pagein.get_PageBackLogin()
    def teardown(self):
        Driver.quit_driver()
    # @parameterized.expand(get_data('back_login.json'))
    @pytest.mark.parametrize('user,pwd,expect', get_data('back_login.json'))
    def test_back_login(self,user,pwd,expect):
        self.PageBackLogin.back_login(user,pwd)
        ret=self.driver.current_url
        try:
            assert expect in ret
            print('断言通过，测试后台登录通过')
        except AssertionError:
            self.PageBackLogin.base_get_image()
            Logger().get_logger('login.log').error('断言失败，测试后台登录不通过')
            raise

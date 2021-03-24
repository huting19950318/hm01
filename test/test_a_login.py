import sys
sys.path.append(r"E:\PycharmProjects\hmtt04")
import pytest
# from parameterized import parameterized
import page
from base.getdata import get_data
from base.driver import Driver
from page.page_login import PageLogin
from page.pagein import PageIn
from base.logger import Logger

logger=Logger().get_logger('login.log')
class TestLogin:
    def setup(self):
        self.driver=Driver().get_driver(page.url)
        self.pagein=PageIn(self.driver)
    def teardown(self):
        Driver().quit_driver()
    # @parameterized.expand(get_data('login.json'))
    @pytest.mark.parametrize('user,pwd,ret',get_data('login.json'))
    def test_login(self,user,pwd,ret):
        self.pagein.get_PageLogin().login(user,pwd)
        ret1=self.driver.current_url
        try:
            assert ret in ret1
            print('断言成功，测试前台登录通过')
        except AssertionError:
            logger.error('断言失败，测试前台登录未通过')
            self.pagein.get_PageLogin().get_image()
            raise


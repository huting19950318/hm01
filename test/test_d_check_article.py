import pytest
from time import sleep

import page
from base.driver import Driver
from base.getdata import get_data
from base.logger import Logger
from page.pagein import PageIn
from parameterized import parameterized
class TestCheckArticle:
    def setup(self):
        self.driver=Driver().get_driver(page.url_back)
        self.PageCheckArticle=PageIn(self.driver).get_PageCheckArticle()
        self.PageBackLogin= PageIn(self.driver).get_PageBackLogin()
        self.PageBackLogin.back_login('testid','testpwd123')
    def teardown(cls):
        Driver().quit_driver()

    # @parameterized.expand(get_data('article.json'))
    @pytest.mark.parametrize('title,channel', get_data('article.json'))
    def test_check_article(self,title,channel):
        self.PageCheckArticle.check_article(title,channel)
        ret=self.PageCheckArticle.find_article()
        try:
            assert ret
            print('断言成功，测试审核文章通过')
        except AssertionError:
            self.PageCheckArticle.base_get_image()
            Logger().get_logger('login.log').error('断言失败，测试审核文章不通过')
            raise

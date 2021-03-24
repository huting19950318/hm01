import pytest
from time import sleep

import page
from base.driver import Driver
from base.getdata import get_data
from base.logger import Logger
from page.pagein import PageIn
from parameterized import parameterized

class TestArticle:

    def setup(self):
        self.driver=Driver().get_driver(page.url)
        self.pagein=PageIn(self.driver)
        self.PageArticle=self.pagein.get_PageArticle()
        self.PageLogin=self.pagein.get_PageLogin()
        self.PageLogin.login('13911111111','246810')
    def teardown(self):
        Driver.quit_driver()
    @pytest.mark.parametrize('name,content,expect',get_data('content.json'))
    def test_article(self,name,content,expect):
        self.PageArticle.option_content()
        sleep(2)
        self.PageArticle.article(name,content)
        ret =self.PageArticle.get_info()
        sleep(2)
        try:
            assert ret==expect
            print('实际结果为{}，预期结果为{},测试发布文章通过'.format(ret,expect))
        except AssertionError:
            print('实际结果为{}，预期结果为{},测试没有通过'.format(ret, expect))
            self.PageArticle.base_get_image()
            Logger().get_logger('login.log').error('断言失败，测试发布文章没有通过')
            raise


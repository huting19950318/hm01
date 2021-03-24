from time import sleep
import page
from base.logger import Logger
from base.webbase import WebBase


class PageCheckArticle(WebBase):
    def option_info(self):
        self.base_click(page.index)
        sleep(2)
        self.base_option(page.info,page.check)
        sleep(2)
    def input_title(self,title):
        self.base_input(page.title,title)
    def input_channel(self,channel):
        self.base_input(page.channel_type,channel)
    def option_state(self):
        self.base_option(page.state,page.dsh)
    def click_find(self):
        self.base_click(page.find)
        sleep(4)
    def get_id(self):
        return self.base_get_text(page.id)
    def click_pass(self):
        self.base_click(page.pass_btn)
        sleep(1)
    def click_sure(self):
        self.base_click(page.sure_btn)
    def check_article(self,title,channel):
        Logger.get_logger('login.log').info('正在审核文章')
        self.option_info()
        self.input_title(title)
        self.input_channel(channel)
        self.option_state()
        self.click_find()
        self.id=self.get_id()
        self.click_pass()
        self.click_sure()
        sleep(3)

    def find_article(self):
        self.base_option(page.state, page.check_pass)
        self.click_find()

        return self.base_ele_exist(self.id)
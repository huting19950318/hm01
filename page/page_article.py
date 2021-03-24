from time import sleep

import page
from base.logger import Logger
from base.webbase import WebBase

SLEEP = sleep(4)


class PageArticle(WebBase):
    def option_content(self):
        self.base_option(page.content_manage,page.publish_article)

    def input_article_name(self,name):
        self.base_input(page.article_name,name)
    def input_article(self,value):
        self.driver.switch_to.frame('publishTinymce_ifr')
        self.base_input(page.article,value)
        self.driver.switch_to.default_content()
    def click_option_image(self):

        self.base_click(page.option_image)

    def option_channel(self):
        self.base_option(page.channel,page.option_sjk)

    def click_publish(self):
        self.base_click(page.publish)
    def get_info(self):
        return self.base_get_text(page.publish_info)
    def article(self,name,value):
        Logger.get_logger('login.log').info('正在发布文章')
        self.input_article_name(name)
        self.input_article(value)
        self.click_option_image()
        sleep(1)
        self.option_channel()
        sleep(2)
        self.click_publish()


from time import sleep
import page
from base.logger import Logger
from base.webbase import WebBase

logger=Logger().get_logger('login.log')

class PageLogin(WebBase):
    def login_input(self,user):
        self.base_input(page.login_input,user)

    def pwd_input(self,pwd):
        self.base_input(page.pwd_input,pwd)
    def login_click(self):
        self.base_click(page.login_btn)
    def login(self,user,pwd):
        logger.info('正在登录，用户名：{}，密码：{}'.format(user,pwd))
        self.login_input(user)
        self.pwd_input(pwd)
        self.login_click()
        sleep(3)
    def get_image(self):
        self.base_get_image()
    def get_nickname(self):
        return self.base_get_text(page.nickname)
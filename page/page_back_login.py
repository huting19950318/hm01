from time import sleep

import page
from base.logger import Logger
from base.webbase import WebBase


logger=Logger().get_logger('login.log')
class PageBackLogin(WebBase):
    def back_login_input(self, user):
        self.base_input(page.back_login_input, user)

    def back_pwd_input(self, pwd):
        self.base_input(page.back_pwd_input, pwd)
    # def back_code_click(self):
    #     self.base_click(page.back_code_btn)
    def back_login_click(self):
        js="document.getElementById('inp1').disabled=false"
        self.driver.execute_script(js)

        self.base_click(page.back_login_btn)

    def back_login(self,user,pwd):
        logger.info('正在登录，用户名：{}，密码：{}'.format(user, pwd))
        self.back_login_input(user)
        self.back_pwd_input(pwd)
        # self.back_code_click()
        self.back_login_click()
        sleep(3)
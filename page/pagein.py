from page.page_article import PageArticle
from page.page_back_login import PageBackLogin
from page.page_check_article import PageCheckArticle
from page.page_login import PageLogin


class PageIn():
    def __init__(self,driver):
        self.driver=driver
    def get_PageLogin(self):
        return PageLogin(self.driver)
    def get_PageArticle(self):
        return PageArticle(self.driver)
    def get_PageBackLogin(self):
        return PageBackLogin(self.driver)
    def get_PageCheckArticle(self):
        return PageCheckArticle(self.driver)
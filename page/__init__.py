from selenium.webdriver.common.by import By

from . import page_login

"""以下是url"""
url='http://pc-toutiao-python.itheima.net/#/login'
url_back='http://ttmis.research.itcast.cn/#/'
""""以下是登录页面的配置信息"""
login_input=(By.CSS_SELECTOR,'[placeholder="请输入手机号"]')
pwd_input=(By.CSS_SELECTOR,'[placeholder="验证码"]')

# login_btn=(By.CSS_SELECTOR,'.el-button--primary')

login_btn=(By.XPATH,'//*[text()="登录"]')

nickname=(By.CSS_SELECTOR,'.user-name')

"""以下是首页的配置信息"""
content_manage=(By.XPATH,"//*[text()='内容管理']")
publish_article=(By.XPATH,'//li[@class="el-submenu is-opened"]/ul[@class="el-menu el-menu--inline"]/li[1]')

"""以下是发布文章页面配置信息"""
article_name=(By.XPATH,'//div[@class="filter-item el-input"]/input[@class="el-input__inner"]')
article=(By.CSS_SELECTOR,'[data-id="publishTinymce"]')
option_image=(By.XPATH,'//div[@class="el-radio-group"]/label[4]/span[1]')

"""以下是频道选择页面配置信息"""
channel=(By.CSS_SELECTOR,'.el-input--suffix')
option_sjk=(By.XPATH,'//*[text()="数据库"]')
publish=(By.XPATH,'//*[text()="发表"]')

"""发布成功提示信息"""
publish_info=(By.XPATH,'//div[@class="el-message el-message--success"]/p')

""""以下是后台登录页面的配置信息"""
back_login_input=(By.CSS_SELECTOR,'[placeholder="用户名"]')
back_pwd_input=(By.CSS_SELECTOR,'[placeholder="密码"]')
back_code_btn=(By.CSS_SELECTOR,'value="输入用户名点击获取验证码"')
back_login_btn=(By.CSS_SELECTOR,'[value="登 录"]')

"""以下是信息管理页面配置信息"""
index=(By.XPATH,'//*[text()="首 页"]')
info=(By.XPATH,'//*[text()="信息管理"]')
check=(By.XPATH,'//*[text()="内容审核"]')

"""以下是文章审核页面配置信息"""
title=(By.CSS_SELECTOR,'[placeholder="请输入: 文章名称"]')
channel_type=(By.CSS_SELECTOR,'[placeholder="请输入: 频道"]')

state=(By.CSS_SELECTOR,'[placeholder="请选择状态"]')
dsh=(By.XPATH,'//*[text()="待审核"]')
check_pass=(By.XPATH,'//*[text()="审核通过"]')
find=(By.CSS_SELECTOR,'.find')

id=(By.XPATH,'//td[@class="el-table_2_column_5  "]/div[@class="cell"]')
pass_btn=(By.XPATH,'//*[text()="通过"]')
sure_btn=(By.CSS_SELECTOR,'.el-button--primary')





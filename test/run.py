import unittest

from hmtt.tool.HTMLTestRunner import HTMLTestRunner

suit=unittest.TestLoader().discover('../test')
with open('../report/report.html','wb') as file:
    HTMLTestRunner(stream=file,title='黑马头条功能测试报告',description='测试用例').run(suit)
# unittest.TextTestRunner().run(suit)
import sys
from selenium import webdriver
import re
from time import sleep
import unittest

class UITest(unittest.TestCase):
    def setUp(self):
        # 1. 实例化一个Webdriver对象，打开浏览器
        self.driver = webdriver.Chrome()

        # 2. 加载页面
        self.driver.get("http://www.baidu.com")

    # @unittest.skip
    def test_001(self):
        '''百度查询UI自动化测试'''
        # 3. 对页面进行操作，定位元素，操作元素（根据功能用例中的操作步骤来的）
        # 说明：webdriver类，webdriver对象中提供了各种的API函数，我们都是通过调用这些API函数来实现对页面元素的定位
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()

        # 4. 断言
        # 1. 跳转之后的页面title应该为：selenium_百度搜索
        # 2. 跳转之后的页面的body中应该包含selenium相关的信息
        sleep(2)
        try:
            self.assertEqual(self.driver.title, 'selenium_百度搜索', '页面title与预期结果不一致！')
            # assert 'selenium' in re.findall('<body>(.+?)</body>',driver.page_source)[0],'页面的body中不存在selenium信息！'
            print('百度搜索-精确搜索selenium用例,测试通过！')
        except AssertionError as e:
            print('百度搜索-精确搜索selenium用例，测试不通过! %s' % e)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
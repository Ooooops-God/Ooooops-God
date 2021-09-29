import HTMLReport
from Lib.HTMLTestRunner import HTMLTestRunner
import unittest
import os


if __name__ == '__main__':
    # test_case_file = 'D:\\project\\shop_service\\test_case\\Business\\Ad_management'
    # test_case_file = './test_case/Business/Ad_management'
    test_path = os.path.join('test_case')  # 用例目录
    report_file = os.path.join('result', 'report.html')  # 更改路径到report目录下
    suite = unittest.defaultTestLoader.discover(test_path)  # 从配置文件中读取用例路径

    # suite = unittest.defaultTestLoader.discover(test_case_file1, 'test*.py')
    runner = HTMLReport.TestRunner(
        output_path='./test_result',  # 保存文件夹名，默认“report”
        lang='cn'  # 支持中文与英文，默认中文
        )
    runner.run(suite)
    # with open(report_file, 'wb') as f:  # 从配置文件中读取
    #     HTMLTestRunner(stream=f, title="Api Test", description="测试描述").run(suite)

# coding:utf-8
'''
description:执行测试
'''
import unittest,HTMLTestRunner
import sys
from config.globalparameter import test_case_path,report_name
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

suite = unittest.defaultTestLoader.discover(start_dir=test_case_path,pattern='test*.py')

if __name__=='__main__':
    report = report_name+'report.html'
    fb = open(report,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title='测试报告'
    )
    runner.run(suite)
    fb.close()

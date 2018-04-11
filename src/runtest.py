# coding:utf-8
'''
description:执行测试
'''
import unittest,HTMLTestRunner
import sys,time
from config.globalparameter import test_case_path,report_name
from src.common import send_email
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
    time.sleep(20)  # 设置睡眠时间，等待测试报告生成完毕（这里被坑了＝＝）
    email = send_email.send_email()
    email.sendReport()

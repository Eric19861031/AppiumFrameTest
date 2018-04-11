# coding:utf-8
'''
description:简单测试内容检测
'''
import unittest

from src.pages import Main_page
from src.common import driver_configue

class test_appium(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = driver_configue.driver_configure().get_driver()

    def test_ClickWebankMainPage(self):
        operation = Main_page.Main_page(self.driver)
        operation.click_commercial()
        operation.click_invest()
        operation.click_transfer()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

# if __name__=='__main__':
#     unittest.main()
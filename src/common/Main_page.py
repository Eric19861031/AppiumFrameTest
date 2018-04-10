# coding:utf-8
'''
main_page 首页
'''
from appium.webdriver.common import mobileby
from src.common.Base_page import Base_page
from src.common.driver_configue import driver_configure


class Main_page(Base_page):
    by = mobileby.MobileBy()
    summary_loc = (by.LINK_TEXT,"总览")
    commercial_loc = (by.LINK_TEXT,"理财")
    invest_loc = (by.LINK_TEXT,"投资")
    transfer_loc = (by.LINK_TEXT, "转账")

    def click_commercial(self):
        self.find_element(*self.commercial_loc).click()

    def click_invest(self):
        self.find_element(*self.invest_loc).click()

    def click_transfer(self):
        self.find_element(*self.transfer_loc).click()

if __name__=='__main__':
    drive = driver_configure().get_driver()
    operation = Main_page(drive)
    operation.click_invest()
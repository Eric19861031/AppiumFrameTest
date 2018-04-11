# coding:utf-8
'''
main_page 首页
'''
from appium.webdriver.common import mobileby
from src.common.Base_page import Base_page
from src.common.driver_configue import driver_configure


class Main_page(Base_page):
    by = mobileby.MobileBy()
    summary_loc = (by.XPATH,"//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]")
    commercial_loc = (by.XPATH,"//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[2]")
    invest_loc = (by.XPATH,"//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[3]")
    transfer_loc = (by.XPATH, "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]")

    def click_commercial(self):
        self.find_element(*self.commercial_loc).click()

    def click_invest(self):
        self.find_element(*self.invest_loc).click()

    def click_transfer(self):
        self.find_element(*self.transfer_loc).click()

if __name__=='__main__':
    drive = driver_configure().get_driver()
    operation = Main_page(drive)
    operation.click_commercial()
    operation.click_invest()
    operation.click_transfer()
